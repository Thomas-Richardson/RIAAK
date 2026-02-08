import os
import hashlib
import json
import re
import unicodedata
import frontmatter
from urllib.parse import quote
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from langchain_text_splitters import MarkdownHeaderTextSplitter

# Configuration
INDEX_NAME = "digital-garden"
NOTES_PATH = "src/site/notes" 
EMBEDDING_MODEL = "text-embedding-3-small"

# Initialize Clients
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_file_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest() # turns notes to unique hashes. whenever the note changes, the hash changed and that's how we know to update the embedding (or not to, which saves money)

def get_embedding(text):
    response = client.embeddings.create(input=text, model=EMBEDDING_MODEL)
    return response.data[0].embedding

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
    """Remove vectors from Pinecone for notes that no longer exist in the vault."""
    deleted_count = 0
    # List all vectors in the index by querying for all unique file_paths
    # Pinecone serverless supports listing vector IDs
    for ids_batch in index.list():
        if not ids_batch:
            continue
        # Fetch metadata for these vectors
        fetch_response = index.fetch(ids=list(ids_batch))
        file_paths_to_delete = set()
        for vec_id, vec_data in fetch_response.vectors.items():
            file_path = vec_data.metadata.get("file_path")
            if file_path and file_path not in current_paths:
                file_paths_to_delete.add(file_path)

        for file_path in file_paths_to_delete:
            print(f"Removing deleted note from index: {file_path}")
            try:
                index.delete(filter={"file_path": {"$eq": file_path}})
                deleted_count += 1
            except Exception as e:
                print(f"Warning: Could not delete vectors for {file_path}: {e}")

    if deleted_count:
        print(f"Removed {deleted_count} deleted note(s) from index.")
    else:
        print("No deleted notes to remove.")

def process_vault():
    index = pc.Index(INDEX_NAME)

    # Remove vectors for deleted notes
    current_paths = get_all_note_paths()
    remove_deleted_notes(index, current_paths)

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
            
            # 2. Check Hash to skip unchanged files
            current_hash = get_file_hash(content)

            # ASCII-fy the path for the ID (Pinecone requirement)
            # This turns "Strässner.md" into "Str%C3%A4ssner.md" for the ID only otherwise wierd characters will crash the model
            ascii_path = quote(relative_path)

            # ID format: "filename.md#0"
            check_id = f"{ascii_path}#0"
            fetch_response = index.fetch(ids=[check_id])

            if check_id in fetch_response.vectors:
                stored_metadata = fetch_response.vectors[check_id].metadata
                stored_hash = stored_metadata.get("file_hash")
                stored_url = stored_metadata.get("url")
                if stored_hash == current_hash and stored_url == permalink:
                    print(f"Skipping {relative_path} (Unchanged)")
                    continue

            print(f"Processing {relative_path}...")
            
            # 3. Delete old chunks for this file
            # Note: Serverless indexes now support delete by metadata filter
            try:
                index.delete(filter={"file_path": {"$eq": relative_path}})
            except Exception as e:
                print(f"Warning: Could not delete old chunks for {relative_path}: {e}")

            # 4. Chunking
            splitter = MarkdownHeaderTextSplitter(
                headers_to_split_on=[("#", "H1"), ("##", "H2"), ("###", "H3")]
            )
            chunks = splitter.split_text(content)
            
            # 5. Embed & Upload
            vectors_to_upsert = []
            for i, chunk in enumerate(chunks):
                # Semantic Boosting: Inject tags into text
                text_to_embed = f"{chunk.page_content}\n\nContext Tags: {', '.join(tags)}"
                vector = get_embedding(text_to_embed)

                # Metadata for the frontend
                metadata = {
                    "file_path": relative_path,
                    "file_hash": current_hash,
                    "text": chunk.page_content,
                    "tags": tags,
                    "url": permalink
                }
                
                # Merge header metadata (H1, H2...)
                metadata.update(chunk.metadata)
                
                vectors_to_upsert.append({
                    "id": f"{ascii_path}#{i}",
                    "values": vector,
                    "metadata": metadata
                })
            
            if vectors_to_upsert:
                index.upsert(vectors=vectors_to_upsert)

if __name__ == "__main__":
    setup_index()
    process_vault()
