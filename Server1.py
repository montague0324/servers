from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 1234

#Handle requests from browser
class myHandler(BaseHTTPRequestHandler):
	
  #Handler for the GET requests
  def do_GET(self):
    try:
      self.send_response(200)
      self.send_header('Content-type','text/html')
      self.end_headers()
      # Send html
      self.wfile.write("Hello")
    except:
      print "!!except clause!!"
    return

def main():
  try:
    #Create a web server and set handler
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Httpserver started on port ' , PORT_NUMBER, " use <Ctrl-C> to stop."
	
    #Wait forever for incoming http requests
    server.serve_forever()

  except KeyboardInterrupt:
    print '^C received, shutting down server'
    server.socket.close()

if __name__ == '__main__':
    main()
