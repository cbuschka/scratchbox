#!/usr/bin/python
# from https://docs.python.org/2/library/simplehttpserver.html
# or python -m SimpleHTTPServer 8080
import SimpleHTTPServer
import SocketServer

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

