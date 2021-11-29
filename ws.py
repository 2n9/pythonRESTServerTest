import http.server
import socketserver

def start():
    port = 8080
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("starting port", port)
        httpd.serve_forever()