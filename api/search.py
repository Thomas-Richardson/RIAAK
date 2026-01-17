from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import os
from pinecone import Pinecone
from openai import OpenAI

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        # Parse query params
        query_components = parse_qs(urlparse(self.path).query)
        user_query = query_components.get('q', [None])[0]

        if not user_query:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Missing query parameter 'q'"}).encode())
            return

        try:
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
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"results": matches}).encode())

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())