import socket
sock = socket.socket()
host = socket.gethostname()
port = 11111
sock.bind((host, port))

sock.listen(5)
i = 0
while True:
   client_sock, client_addr = sock.accept()
   print(client_addr, "coming in\n") 
   client_sock.send(bytes("successfuly connect the server\n", encoding='utf-8'))
   str0 = "the " + str(i) + " connection"
   print(type(str0))
   client_sock.send(bytes(str0, encoding='utf-8') )
   i = i+1
   client_sock.send(b'\nHello ABC\n')

   client_sock.close()
