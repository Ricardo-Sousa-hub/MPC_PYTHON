import socket

# create a socket
s = socket.socket()

# connect to server 3
s.connect(('127.0.0.1', 9000))

# send a message to server 3
s.send('Hello from client'.encode())

# receive the response from server 3
data = s.recv(1024)
print('Server 3 response:', data.decode())

# close the socket
s.close()
