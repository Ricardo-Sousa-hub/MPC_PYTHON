import socket
import time
import random as r

IP = socket.gethostbyname(socket.gethostname())
PORT = 8002
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "3"

ADDR_SERVER3 = (IP, 8003)
ADDR_CLIENT = (IP, 8000)


def main():
    executed = False
    print("[STARTING] Server is starting ...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    print("Trying to connect to server 3")

    connected = False
    while True:
        try:
            if not connected:
                server.connect(ADDR_SERVER3)
                print("Connection to server 3 successful")
                connected = True
        except:
            if not connected:
                print("Trying to connect to server 3...")
                time.sleep(5)

        if connected and not executed:
            k = int(server.recv(SIZE).decode(FORMAT))
            server.send(("Server 2: K recebido").encode(FORMAT))
            y = r.randint(0, 101)
            print(f"Y -> Numero gerado aleatoriamente: {y}")
            print(f"K: {k}")
            print(f"K + X = {y+k}")
            y = bin(y + k)
            print(y)
            executed = True


if __name__ == "__main__":
    main()
