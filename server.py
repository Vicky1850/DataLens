#!/usr/bin/env python3
"""
Multi-Excel Search — Local Server
Run: python server.py
Then open: http://localhost:8080
"""
import http.server
import socketserver
import webbrowser
import os
import threading

PORT = 8080
DIR  = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, fmt, *args):
        pass  # silence request logs

def open_browser():
    import time; time.sleep(0.5)
    webbrowser.open(f"http://localhost:{PORT}")

print(f"\n  Multi-Excel Search is running!")
print(f"  Open: http://localhost:{PORT}")
print(f"  Press Ctrl+C to stop\n")

threading.Thread(target=open_browser, daemon=True).start()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
