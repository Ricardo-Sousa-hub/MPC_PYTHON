import socket
import time
import random as r
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 8001
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "3"

ADDR_SERVER3 = (IP, 8003)
ADDR_CLIENT = (IP, 8000)
x = 0


def handle_client(conn, addr):
    global x
    print("Conectado ao client")
    conn.send(str(x).encode(FORMAT))
    print("Valor x enviado ao client")
    conn.close()
    main()


def main():
    global x
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
            server.send(("Server 1: K recebido").encode(FORMAT))
            x = r.randint(0, 101)
            print(f"X  -> Numero gerado aleatoriamente: {x}")
            print(f"K: {k}")
            print(f"K + X = {x+k}")
            x = bin(x + k)
            print(x)
            executed = True

        server.close()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()
        print("Server 1 a procura do client...")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()


if __name__ == "__main__":
    main()
