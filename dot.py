import http.server
import socketserver
import json

s = open("settings.json")
settings = json.load(s)
p = int(settings["port"])

PORT = p
DIRECTORY = "SOURCE"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()