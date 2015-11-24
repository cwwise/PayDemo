# coding: UTF-8
__author__ = 'weiwei'

import cwweixinpay
from http.server import BaseHTTPRequestHandler,HTTPServer



PORT_NUMBER = 9192
hostName = "localhost"

# This class will handle any incoming request from
# a browser
class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        print ('Get request received')
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        jsonString = cwweixinpay.weixinpayactionDemo()
        self.wfile.write(jsonString.encode())
        # self.wfile.write("Hello World !".encode())
        return
    def do_POST(self):
        print ('Post request received')
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        jsonString = cwweixinpay.weixinpayactionDemo()
        self.wfile.write(jsonString.encode())
        return

try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer((hostName, PORT_NUMBER), myHandler)
    print ('Started httpserver on port ' , PORT_NUMBER)

    # Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print ('^C received, shutting down the web server')
    server.socket.close()