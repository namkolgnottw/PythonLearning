import socket

sock = socket.socket()
host = socket.gethostname()
port = 11111

sock.connect((host, port))
b= sock.recv(4096)
print(type(b))
print(str(b, encoding='utf-8'))
sock.close()