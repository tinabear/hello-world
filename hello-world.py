#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    ./hello-world.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request with son ::
    curl -d '{"name": "bar"}' http://localhost

"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer, simplejson

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("Hello World!")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

#        self.send_response(200)
#        self.end_headers()
        data = simplejson.loads(self.data_string)
        self.wfile.write("Hello %s World!" %(data["name"]))
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
