import socket
import time
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "3"
ADDR_SERVER1 = (IP, 8001)
ADDR_SERVER2 = (IP, 8002)
ADDR_SERVER3 = (IP, 8003)

x = "null"
y = "null"

# server1 = "x"
# server2 = "y"
connected = False
conS1 = False
conS2 = False


def escreverMenu():
    print("1 - >")
    print("2 - <")
    print("3 - Disconnect")


def analisarInput(x, y, op):
    if op == "1":
        if len(x) > len(y):
            print("Server 1(X) > Server 2(Y)")
        if len(x) < len(y):
            print("Server 2(Y) > Server 1(X)")
        if len(x) == len(y):
            index = 0
            for i in range(2, len(x)-1):
                if int(x[i]) > int(y[index]):
                    print("Server 1(X) > Server 2(Y)")
                    break
                if int(x[i]) < int(y[index]):
                    print("Server 2(Y) > Server 1(X)")
                    break
                index += 1
    else:
        if len(x) > len(y):
            print("Server 2(Y) < Server 1(X)")
        if len(x) < len(y):
            print("Server 1(X) < Server 2(Y)")
        if len(x) == len(y):
            index = 0
            for i in range(2, len(x)-1):
                if int(x[i]) > int(y[index]):
                    print("Server 2(Y) < Server 1(X)")
                    break
                if int(x[i]) < int(y[index]):
                    print("Server 1(X) > Server 2(Y)")
                    break
                index += 1


def main():
    executing = True
    global conS1
    global conS2
    global connected
    global y
    while executing:
        conS1 = False
        conS2 = False
        connected = False
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.bind(ADDR)

        while not connected:
            try:
                client.connect(ADDR_SERVER3)
                if not connected:
                    connected = True
            except:
                print("Trying to connect to server 3...")
                time.sleep(3)

        print(f"[CONNECTED] Client connected to Server 3")

        while connected:
            escreverMenu()
            op = input("-> ")

            if not op.isnumeric() or int(op) > 3 or int(op) < 1:
                print("Digite uma opcao valida!")
            else:
                client.send(op.encode(FORMAT))
                if op == DISCONNECT_MSG:
                    print("Client disconnected...")
                    connected = False
                    executing = False
                else:
                    msg = client.recv(SIZE).decode(FORMAT)
                    if msg == "Wait for server 1 and 2 to be connected":
                        print(msg)
                    else:
                        client.send(DISCONNECT_MSG.encode(FORMAT))
                        client.close()

                        connected = False
        if executing:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.bind(ADDR)

            #Server 2
            while not conS1:
                try:
                    client.connect(ADDR_SERVER1)
                    if not conS1:
                        conS1 = True
                except:
                    print("Trying to connect to server 1...")
                    time.sleep(5)
            print("Connected to Server 1!")

            while conS1:
                msg = client.recv(SIZE).decode(FORMAT)
                if msg.isalnum():
                    y = msg
                    print(f"MSG server 1: {y}")
                    conS1 = False
            time.sleep(5)
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.bind(ADDR)

            #Server 1
            while not conS2:
                try:
                    client.connect(ADDR_SERVER2)
                    if not conS2:
                        conS2 = True
                except:
                    print("Trying to connect to server 2...")
                    time.sleep(5)
            print("Connected to Server 2!")

            while conS2:
                msg = client.recv(SIZE).decode(FORMAT)
                if msg.isalnum():
                    y = msg
                    print(f"MSG server 2: {y}")
                    conS2 = False

            analisarInput(x, y, op)


if __name__ == "__main__":
    main()
