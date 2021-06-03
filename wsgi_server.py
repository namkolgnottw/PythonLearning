
class WSGIServer():
   def __init__(self, server_addr):
      self.listen_socket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
      listen_socket.setsockopt(sock.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      listen_socket.bind(server_addr)
      listen_socket.listen(5)
      host, port = self.listen_socket.getsockname()[:2]
      self.server_name = socket.getfqdn(host)
      self.server_port = port
      self.headers_set = []
      self.application = None
      self.client_connection = None
      self.request_data = None
      self.request_method = None
      self.path = None
      self.request_version = None


   def _handle_one_request(self):
      environ = _get_environ
      pass

   def serve_forever():
      while (True):
         socket = self.listen_socket.accept()
         s = _handle_one_request()
         _finish_response()


