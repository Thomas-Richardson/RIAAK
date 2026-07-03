import os
import argparse
import hashlib
import json
import re
import unicodedata
import frontmatter
from urllib.parse import quote, unquote
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

# Configuration
INDEX_NAME = "digital-garden"
NOTES_PATH = "src/site/notes"
EMBEDDING_MODEL = "text-embedding-3-small"

# Bump when the chunking / embedding-text format changes so stale-format vectors
# can be detected. --force re-ingests everything with the current schema.
SCHEMA_VERSION = 2

# Chunking: split on headers first (preserves the H1/H2/H3 breadcrumb), then
# bound each section so no chunk exceeds the embedding model's 8,191-token limit
# and each stays within the reranker's ~1024-token query+passage budget.
# 1500 chars ~ 350-400 tokens; 200 overlap keeps sentences continuous.
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 200

# Batch sizes: OpenAI embeddings accept up to 2,048 inputs / 300k tokens per
# request; 100 bounded chunks is comfortably under both. Pinecone fetch accepts
# large ID lists; 200 keeps requests small.
EMBED_BATCH_SIZE = 100
FETCH_BATCH_SIZE = 200

# Initialize Clients
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def get_file_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest() # turns notes to unique hashes. whenever the note changes, the hash changed and that's how we know to update the embedding (or not to, which saves money)


def get_embeddings(texts, batch_size=EMBED_BATCH_SIZE):
    """Embed a list of texts, batching API calls. Preserves input order."""
    out = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        response = client.embeddings.create(input=batch, model=EMBEDDING_MODEL)
        # The API may return items out of order; sort by index to be safe.
        ordered = sorted(response.data, key=lambda d: d.index)
        out.extend(d.embedding for d in ordered)
    return out


def slugify_text(value):
    # Mirror Eleventy slugify behavior closely enough for URL fallbacks.
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.lower()
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text)
    return ascii_text.strip("-")


def setup_index():
    # Create index if it doesn't exist
    if INDEX_NAME not in [i.name for i in pc.list_indexes()]:
        print(f"Creating index {INDEX_NAME}...")
        pc.create_index(
            name=INDEX_NAME,
            dimension=1536, # Matches text-embedding-3-small
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )


def get_all_note_paths():
    """Collect all relative paths of markdown files in the vault."""
    paths = set()
    for root, _, files in os.walk(NOTES_PATH):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, NOTES_PATH)
                paths.add(relative_path)
    return paths


def remove_deleted_notes(index, current_paths):
    """Remove vectors for notes that no longer exist in the vault.

    Vector IDs encode the URL-quoted relative path ("<quoted path>#<chunk>"),
    so we can derive the note path directly from the ID without fetching
    metadata for every vector.
    """
    deleted = set()
    for ids_batch in index.list():
        if not ids_batch:
            continue
        for vec_id in ids_batch:
            relative_path = unquote(vec_id.split("#")[0])
            if relative_path not in current_paths:
                deleted.add(relative_path)

    for relative_path in deleted:
        print(f"Removing deleted note from index: {relative_path}")
        try:
            index.delete(filter={"file_path": {"$eq": relative_path}})
        except Exception as e:
            print(f"Warning: Could not delete vectors for {relative_path}: {e}")

    if deleted:
        print(f"Removed {len(deleted)} deleted note(s) from index.")
    else:
        print("No deleted notes to remove.")


def prefetch_hashes(index, ascii_paths):
    """Batch-fetch the '#0' vector for each note to read its stored hash/url.

    Returns {vector_id: metadata} so process_vault can skip unchanged notes
    without one fetch round-trip per file.
    """
    stored = {}
    check_ids = [f"{p}#0" for p in ascii_paths]
    for i in range(0, len(check_ids), FETCH_BATCH_SIZE):
        batch = check_ids[i:i + FETCH_BATCH_SIZE]
        try:
            resp = index.fetch(ids=batch)
        except Exception as e:
            print(f"Warning: hash prefetch batch failed: {e}")
            continue
        for vec_id, vec in resp.vectors.items():
            stored[vec_id] = vec.metadata
    return stored


def process_vault(force=False):
    index = pc.Index(INDEX_NAME)

    if force:
        print("--force: deleting all vectors and re-embedding from scratch...")
        try:
            index.delete(delete_all=True)
        except Exception as e:
            print(f"Warning: delete_all failed (index may be empty): {e}")
        stored_hashes = {}
    else:
        # Remove vectors for deleted notes
        current_paths = get_all_note_paths()
        remove_deleted_notes(index, current_paths)
        # Pre-fetch stored hashes for all notes in one batched pass.
        ascii_paths = [quote(p) for p in current_paths]
        stored_hashes = prefetch_hashes(index, ascii_paths)

    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("#", "H1"), ("##", "H2"), ("###", "H3")]
    )
    sub_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )

    # Iterate through all markdown files
    for root, _, files in os.walk(NOTES_PATH):
        for file in files:
            if not file.endswith(".md"):
                continue

            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, NOTES_PATH)

            # 1. Parse Content
            with open(file_path, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)

            content = post.content
            tags = post.get("tags", [])

            # --- Sanitize Tags ---
            # Handle case where tags is None
            if tags is None:
                tags = []
            # Handle comma-separated string
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(',')]
            # Handle list containing None or non-string items
            tags = [str(t) for t in tags if t is not None and str(t).strip() != ""]

            permalink = post.get("permalink")
            if not permalink:
                file_slug = os.path.splitext(os.path.basename(relative_path))[0]
                permalink = f"/notes/{slugify_text(file_slug)}/"
            if "gardenEntry" in tags:
                permalink = "/"

            title = os.path.splitext(os.path.basename(relative_path))[0]

            # 2. Check Hash to skip unchanged files
            current_hash = get_file_hash(content)

            # ASCII-fy the path for the ID (Pinecone requirement)
            # This turns "Strässner.md" into "Str%C3%A4ssner.md" for the ID only otherwise wierd characters will crash the model
            ascii_path = quote(relative_path)

            if not force:
                stored_metadata = stored_hashes.get(f"{ascii_path}#0")
                if stored_metadata:
                    stored_hash = stored_metadata.get("file_hash")
                    stored_url = stored_metadata.get("url")
                    stored_schema = stored_metadata.get("schema_version")
                    if (stored_hash == current_hash
                            and stored_url == permalink
                            and stored_schema == SCHEMA_VERSION):
                        print(f"Skipping {relative_path} (Unchanged)")
                        continue

            print(f"Processing {relative_path}...")

            # 3. Delete old chunks for this file (handles chunk-count shrink so
            # no orphaned #i vectors remain). Skipped under --force (delete_all
            # already cleared everything).
            if not force:
                try:
                    index.delete(filter={"file_path": {"$eq": relative_path}})
                except Exception as e:
                    print(f"Warning: Could not delete old chunks for {relative_path}: {e}")

            # 4. Chunking: header split, then bound each section.
            header_chunks = header_splitter.split_text(content)
            sub_chunks = []          # list of (text, header_metadata)
            for hc in header_chunks:
                for piece in sub_splitter.split_text(hc.page_content):
                    sub_chunks.append((piece, hc.metadata))

            if not sub_chunks:
                continue

            # 5. Build enriched embedding text (title + header breadcrumb +
            # chunk + context tags), embed in batches, and collect vectors.
            def make_breadcrumb(header_meta):
                parts = [title] + [header_meta[h] for h in ("H1", "H2", "H3") if h in header_meta]
                return " > ".join(parts)

            texts_to_embed = [
                f"{make_breadcrumb(hm)}\n\n{text}\n\nContext Tags: {', '.join(tags)}"
                for text, hm in sub_chunks
            ]

            embeddings = get_embeddings(texts_to_embed)

            vectors_to_upsert = []
            for i, ((text, header_meta), vector) in enumerate(zip(sub_chunks, embeddings)):
                # Store the raw chunk as `text` (clean quotes/excerpts); keep
                # title/breadcrumb as separate metadata fields.
                metadata = {
                    "file_path": relative_path,
                    "file_hash": current_hash,
                    "text": text,
                    "tags": tags,
                    "url": permalink,
                    "title": title,
                    "breadcrumb": make_breadcrumb(header_meta),
                    "schema_version": SCHEMA_VERSION,
                }
                # Merge header metadata (H1, H2...)
                metadata.update(header_meta)

                vectors_to_upsert.append({
                    "id": f"{ascii_path}#{i}",
                    "values": vector,
                    "metadata": metadata,
                })

            if vectors_to_upsert:
                index.upsert(vectors=vectors_to_upsert)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest the vault into Pinecone.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Delete all vectors and re-embed every note (ignores hash cache).",
    )
    args = parser.parse_args()

    setup_index()
    process_vault(force=args.force)
