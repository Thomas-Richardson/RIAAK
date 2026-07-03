from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import os

# --- Module-level configuration ---
INDEX_NAME = "digital-garden"
EMBEDDING_MODEL = "text-embedding-3-small"
RERANK_MODEL = "bge-reranker-v2-m3"

# How many candidates to pull from Pinecone before reranking. We over-fetch so
# that after reranking + de-duplicating by note we still have enough distinct
# notes to fill the requested top_k.
CANDIDATE_POOL = 30
DEFAULT_TOP_K = 8
MAX_TOP_K = 15
COMPACT_TEXT_CHARS = 400          # snippet length when ?compact=1
RERANK_DOC_CHARS = 2000           # per-doc text cap sent to the reranker

# Lazily-constructed, module-scoped clients. On a warm serverless invocation
# these are reused, so we skip re-importing/re-connecting (saves ~100-300ms and
# reuses HTTPS connection pools). Construction is deferred to the first request
# so that a missing env var surfaces as a JSON 500 rather than an import crash.
_clients = {}


def get_clients():
    if not _clients:
        from pinecone import Pinecone
        from openai import OpenAI

        if "PINECONE_API_KEY" not in os.environ:
            raise EnvironmentError("PINECONE_API_KEY not set")
        if "OPENAI_API_KEY" not in os.environ:
            raise EnvironmentError("OPENAI_API_KEY not set")

        pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
        _clients["pc"] = pc
        _clients["index"] = pc.Index(INDEX_NAME)
        _clients["openai"] = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    return _clients


def _title_from_path(file_path):
    """Derive a readable title from a note's file path when no title metadata."""
    if not file_path:
        return ""
    base = file_path.replace("\\", "/").split("/")[-1]
    if base.lower().endswith(".md"):
        base = base[:-3]
    return base


def run_search(user_query, top_k=DEFAULT_TOP_K, compact=False):
    """Core search pipeline: embed -> retrieve -> rerank -> dedupe by note.

    Returns a list of result dicts: {score, text, url, file_path, title, tags}.
    Importable so it can be smoke-tested locally without the HTTP layer.
    """
    clients = get_clients()
    index = clients["index"]
    openai_client = clients["openai"]
    pc = clients["pc"]

    top_k = max(1, min(int(top_k), MAX_TOP_K))

    # 1. Embed the query
    res = openai_client.embeddings.create(input=user_query, model=EMBEDDING_MODEL)
    query_vector = res.data[0].embedding

    # 2. Retrieve a candidate pool from Pinecone
    query_res = index.query(
        vector=query_vector,
        top_k=CANDIDATE_POOL,
        include_metadata=True,
    )
    matches = list(query_res.get("matches", []))
    if not matches:
        return []

    # 3. Rerank the candidate pool against the query (best-effort). The reranker
    # scores true query/passage relevance, which is far better than raw cosine
    # for surfacing the most useful chunk. On any failure we keep vector order.
    try:
        documents = []
        for m in matches:
            text = (m["metadata"].get("text") or "")[:RERANK_DOC_CHARS]
            documents.append({"id": m["id"], "text": text})

        rr = pc.inference.rerank(
            model=RERANK_MODEL,
            query=user_query,
            documents=documents,
            top_n=len(documents),
            return_documents=False,
            parameters={"truncate": "END"},
        )
        # rr.data is ordered best-first; each row has .index into `documents`
        matches = [matches[row.index] for row in rr.data]
    except Exception as e:
        # Fall back to vector order; log for Vercel diagnostics.
        print(f"Rerank failed, using vector order: {e}")

    # 4. De-duplicate by note (url), keeping the best-ranked chunk per note.
    # This directly helps the LLM/skill consumer, which does not dedupe and
    # would otherwise burn tokens on multiple chunks of the same note. The
    # website also collapses to one card per note, so this is a strict win
    # there too, and it maximizes source diversity in the results.
    seen = set()
    results = []
    for m in matches:
        meta = m["metadata"]
        url = meta.get("url", "")
        if url in seen:
            continue
        seen.add(url)

        text = meta.get("text", "")
        if compact and len(text) > COMPACT_TEXT_CHARS:
            text = text[:COMPACT_TEXT_CHARS].rstrip() + "…"

        file_path = meta.get("file_path", "")
        results.append({
            "score": m.get("score"),
            "text": text,
            "url": url,
            "file_path": file_path,
            "title": meta.get("title") or _title_from_path(file_path),
            "tags": meta.get("tags", []),
        })
        if len(results) >= top_k:
            break

    return results


class handler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        """Helper to send CORS headers for every response"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()
        return

    def do_GET(self):
        try:
            # Parse query params
            query_components = parse_qs(urlparse(self.path).query)
            user_query = query_components.get('q', [None])[0]

            if not user_query:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Missing query parameter 'q'"}).encode())
                return

            # Optional params
            try:
                top_k = int(query_components.get('top_k', [DEFAULT_TOP_K])[0])
            except (ValueError, TypeError):
                top_k = DEFAULT_TOP_K
            compact = query_components.get('compact', ['0'])[0] in ('1', 'true', 'yes')

            matches = run_search(user_query, top_k=top_k, compact=compact)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            # Let Vercel's CDN serve repeated identical queries without invoking
            # the function. Ingestion runs on push, so 1h freshness is fine.
            self.send_header('Cache-Control', 'public, s-maxage=3600, stale-while-revalidate=86400')
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"results": matches}).encode())

        except Exception as e:
            # Catch crashes and send them as JSON so we can debug
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self._send_cors_headers()
            self.end_headers()
            error_response = {
                "error": str(e),
                "type": type(e).__name__
            }
            self.wfile.write(json.dumps(error_response).encode())
