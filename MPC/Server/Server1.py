import socket
import time
import random

IP = socket.gethostbyname(socket.gethostname())
PORT = 8001
ADDR = (IP, PORT)
SERVER3_ADDR = (IP, 8003)
SIZE = 1024
FORMAT = "utf-8"
server_status = False


def GerarN():
    return random.randint(0, 100)


def main():
    connected = False
    print("Starting server 1...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server_status = True
    while server_status:
        try:
            if not connected:
                server.connect(SERVER3_ADDR)
                print("Connection to server 3 successful")
                connected = True
        except:
            if not connected:
                print("Trying to connect to server 3...")
                time.sleep(5)

        if connected:
            server.send(str(GerarN()).encode(FORMAT))
            time.sleep(5)


if __name__ == "__main__":
    main()
