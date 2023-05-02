import socket
import random

s = socket.socket()

s.bind(('127.0.0.1', 8000))

# conectar ao server 3
s.connect(('127.0.0.1', 9000))

rand = random.randint(0, 100)
print(rand)

# enviar mensagem para server 3
s.send(str(rand).encode())

# receber respsta do server 3
data = s.recv(1024)
print('Server 3 response:', data.decode())

s.close()
