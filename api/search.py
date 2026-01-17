from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import os
from pinecone import Pinecone
from openai import OpenAI

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
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Missing query parameter 'q'"}).encode())
                return

            # Initialize Clients
            pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
            client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
            index = pc.Index("digital-garden")

            # Embed Query
            res = client.embeddings.create(input=user_query, model="text-embedding-3-small")
            query_vector = res.data[0].embedding

            # Search Pinecone
            results = index.query(
                vector=query_vector,
                top_k=5,
                include_metadata=True
            )

            # Format Response
            matches = []
            for match in results['matches']:
                matches.append({
                    "score": match['score'],
                    "text": match['metadata'].get('text', ''),
                    "url": match['metadata'].get('url', ''),
                    "file_path": match['metadata'].get('file_path', '')
                })

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
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
