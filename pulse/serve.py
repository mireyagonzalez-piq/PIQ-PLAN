#!/usr/bin/env python3
"""Serve the PIQ Performance Pulse replica locally.
Usage: python3 serve.py [port]
"""
import http.server, socketserver, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8899

class Quiet(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory='/root/piq-pulse-replica', **kw)
    def log_message(self, *a): pass

class S(socketserver.TCPServer):
    allow_reuse_address = True

print(f"Serving http://127.0.0.1:{PORT}/index.html")
S(('127.0.0.1', PORT), Quiet).serve_forever()
