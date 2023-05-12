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
x1 = 0

MIN = 1
MAX = 100

connected = False
clientCon = False


def main():
    global connected
    global x
    global x1
    global clientCon
    executing = True
    while executing:
        clientCon = False
        connected = False
        print("[STARTING] Server 1 is starting ...")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        print("Trying to connect to server 3...")

        while not connected:
            try:
                server.connect(ADDR_SERVER3)
                if not connected:
                    connected = True
            except:
                print("Trying to connect to server 3...")
                time.sleep(5)
        print("Connected to server 3")

        while connected:
            k = server.recv(SIZE).decode(FORMAT)
            if k != "null" and k != "":
                print(f"K: {k}")
                x = r.randint(MIN, MAX)
                print(f"x: {x}")
                server.send(DISCONNECT_MSG.encode(FORMAT))
                x1 = x + int(k)
                print(f"x1: {x1}")

                connected = False

        server.close()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        print("Server 1 is listening...")
        server.listen()

        while not clientCon:
            conn, addr = server.accept()
            if addr[1] == 8000:
                handle_con(conn, addr)


def client(conn, addr):
    global x1
    conn.send(str(bin(x1)).encode(FORMAT))
    print("x1 sended to client...")


def handle_con(conn, addr):
    print("NEW CONNECTION")
    global clientCon
    print("Connected to client!")
    client(conn, addr)
    print("Closing connection to client...")
    conn.close()
    clientCon = True


if __name__ == "__main__":
    main()
