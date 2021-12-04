from threading import Thread
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler, HTTPServer
import time
import asyncio


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        request_data = self.rfile.read(content_length).decode()

        if (self.path != '/api/remote/'):
            print('endereço invalido')
        print(request_data)
        if request_data == 'A\n':
            time.sleep(10)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes(str(request_data), "utf-8"))
        if request_data == 'B\n':
            time.sleep(2)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes(str(request_data), "utf-8"))
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(str(request_data), "utf-8"))

    def do_GET(self):
        # if self.path == '/':
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(str(self.path), "utf-8"))



class ThreadingHTTPServer(ThreadingHTTPServer, HTTPServer):
    daemon_threads = True


def serve_on_port(port):
    server = ThreadingHTTPServer(("localhost", port), Handler)
    print('run')
    server.serve_forever()


Thread(target=serve_on_port, args=[9911]).start()
# serve_on_port(9911)
