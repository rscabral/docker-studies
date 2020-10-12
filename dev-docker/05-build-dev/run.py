import logging
import http.server
import socketserver
import getpass

class CustomHttpHandler(http.server.SimpleHTTPRequestHandler):
  def log_message(self, format, *args):
    logging.info("%s - - [%s] %s\n"% (
      self.client_address[0],
      self.log_date_time_string(),
      format%args
    ))

logging.basicConfig(
  filename='/log/http-server.log',
  format='%(asctime)s - %(levelname)s - %(message)s',
  level=logging.INFO
)
logging.getLogger().addHandler(logging.StreamHandler())
logging.info('Starting...')
PORT = 8000

httpd = socketserver.TCPServer(("", PORT), CustomHttpHandler)
logging.info('Listening port: %s', PORT)
logging.info('User provided by Dockerfile: %s', getpass.getuser())

httpd.serve_forever()
