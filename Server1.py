from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 1234

#This class will handles any incoming request from the browser 
class myHandler(BaseHTTPRequestHandler):
	
  #Handler for the GET requests
  def do_GET(self):
    try:
      self.send_response(200)
      self.send_header('Content-type','text/html')
      self.end_headers()
      # Send the html message
      self.wfile.write("Hello Mike!")
    except:
      print "in the except clause!"
    return

def main():
  try:
    #Create a web server and define the handler to manage the incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER, " use <Ctrl-C> to stop."
	
    #Wait forever for incoming htto requests
    server.serve_forever()

  except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()

if __name__ == '__main__':
    main()
