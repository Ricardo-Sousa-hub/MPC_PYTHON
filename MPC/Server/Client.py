import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 8003
ADDR_SERVER3 = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "3"
CLIENT_ADDR = (IP, 8000)
ADDR_SERVER1 = (IP, 8001)
ADDR_SERVER2 = (IP, 8002)
x = 0
y = 0


def escreverMenu():
    print("1 - >=")
    print("2 - <=")
    print("3 - Disconnect")


def conectarAoServer3(client):
    client.close()
    main()


def conectarAoServer2(client):
    global y
    client.close()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.bind(CLIENT_ADDR)
    client.connect(ADDR_SERVER2)
    print("Conectado ao servidor 2")
    while True:
        y = client.recv(SIZE).decode(FORMAT)
        print(f"Valor enviado pelo server 2: {y}")
        if y != 0:
            break
        conectarAoServer3(client)


def conectarAoServer1(client):
    global x
    client.send(DISCONNECT_MSG.encode(FORMAT))
    client.close()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.bind(CLIENT_ADDR)
    client.connect(ADDR_SERVER1)
    print("Conectado ao servidor 1")
    while True:
        x = client.recv(SIZE).decode(FORMAT)
        print(f"Valor enviado pelo server 1: {x}")
        if x != 0:
            break
    conectarAoServer2(client)


def main():
    connected = False
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.bind(CLIENT_ADDR)
    while not connected:
        try:
            client.connect(ADDR_SERVER3)
            if not connected:
                connected = True
        except:
            print("Trying to connect to server 3")
    print(f"[CONNECTED] Client connected to Server at {IP}:{PORT}")
    connected=True
    while connected:
        escreverMenu()
        op = input("-> ")

        if not op.isnumeric() or int(op) > 3 or int(op) < 1:
            print("Digite uma opcao valida!")
        else:
            client.send(op.encode(FORMAT))
            if op == DISCONNECT_MSG:
                connected = False
            else:
                conectarAoServer1(client)


if __name__ == "__main__":
    main()
