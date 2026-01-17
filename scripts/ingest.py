import os
import hashlib
import json
import frontmatter
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from langchain_text_splitters import MarkdownHeaderTextSplitter

# Configuration
INDEX_NAME = "digital-garden"
NOTES_PATH = "src/site/notes" # <--- CHECK THIS PATH matches your repo
EMBEDDING_MODEL = "text-embedding-3-small"

# Initialize Clients
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_file_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def get_embedding(text):
    response = client.embeddings.create(input=text, model=EMBEDDING_MODEL)
    return response.data[0].embedding

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

def process_vault():
    index = pc.Index(INDEX_NAME)
    
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
            if isinstance(tags, str): tags = [t.strip() for t in tags.split(',')]
            
            # 2. Check Hash to skip unchanged files
            current_hash = get_file_hash(content)
            
            # We check the first chunk of this file to see if the hash matches
            # ID format: "filename.md#0"
            check_id = f"{relative_path}#0"
            fetch_response = index.fetch(ids=[check_id])
            
            if check_id in fetch_response.vectors:
                stored_hash = fetch_response.vectors[check_id].metadata.get("file_hash")
                if stored_hash == current_hash:
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
                    "url": f"/{relative_path.replace('.md', '')}" # Simple URL construction
                }
                
                # Merge header metadata (H1, H2...)
                metadata.update(chunk.metadata)
                
                vectors_to_upsert.append({
                    "id": f"{relative_path}#{i}",
                    "values": vector,
                    "metadata": metadata
                })
            
            if vectors_to_upsert:
                index.upsert(vectors=vectors_to_upsert)

if __name__ == "__main__":
    setup_index()
    process_vault()
