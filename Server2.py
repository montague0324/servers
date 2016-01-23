#!/usr/bin/env python
 
import BaseHTTPServer
import os
 
#Create custom HTTPRequestHandler class
class MyHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  
  def do_GET(self):
    rootdir = 'C:\Users\mike.montague\Documents\Python' #file location
    try:
      if self.path.endswith('.html'):
        f = open(rootdir + self.path) #open requested file
 
        #send code 200 response
        self.send_response(200)
 
        #send header
        self.send_header('Content-type','text-html')
        self.end_headers()
 
        #send file content to client
        self.wfile.write(f.read())
        f.close()
        return
      
    except IOError:
      self.send_error(404, 'file not found')
  
def run():
  print('http server is starting...')
 
  #Create server. Default port is 80
  server_address = ('127.0.0.1', 1234)
  httpd = BaseHTTPServer.HTTPServer(server_address, MyHTTPRequestHandler)
  print('http server running...')
  httpd.serve_forever()
  
if __name__ == '__main__':
  run()