from aula import MyWebServer
from http.server import SimpleHTTPRequestHandler
import os

PORT = (os.getenv('PORT') or 3001)

class ManuseioHttpRequest(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<p>Olá Mundo!</p>".encode())
        elif self.path == "/pagina1":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<p>Estou numa nova pagina!</p>".encode())
        elif self.path == "/index":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            res_body = open('index.html', "r").read().format_map({
                "PORT":PORT
            })
            self.wfile.write(res_body.encode())
        else:
            self.send_error(418)

app = MyWebServer(ManuseioHttpRequest)

if __name__ == "__main__":
    app.run()