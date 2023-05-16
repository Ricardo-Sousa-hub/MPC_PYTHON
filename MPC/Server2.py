import socket
import time
import random as r

IP = socket.gethostbyname(socket.gethostname())
PORT = 8002
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "3"

ADDR_SERVER4 = (IP, 8004)
ADDR_SERVER3 = (IP, 8003)

y = 0
y1 = 0

MIN = 1
MAX = 100

connected = False
clientCon = False


def main():
    global connected
    global y
    global y1
    global clientCon
    executing = True
    while executing:
        server4 = False
        clientCon = False
        connected = False
        print("[STARTING] Server 2 is starting ...")
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
                y = r.randint(MIN, MAX)
                print(f"y: {y}")
                server.send(DISCONNECT_MSG.encode(FORMAT))
                y1 = y + int(k)
                print(f"y1: {y1}")

                connected = False

        server.close()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        print("Server 1 is trying to connect to server 4...")

        while not server4:
            try:
                server.connect(ADDR_SERVER4)
                if not server4:
                    server4 = True
            except:
                print("Trying to connect to server 4...")
                time.sleep(5)
        print("Connected to server 4")

        server.send(str(bin(y1)).encode(FORMAT))
        server.close()


if __name__ == "__main__":
    main()
