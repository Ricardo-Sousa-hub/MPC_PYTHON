import socket
import threading
import random
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 6001
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "Disconnected!"


def GerarSend(server):
    rand = random.randint(0, 100)
    print(rand)
    data = str(rand).encode()
    server.send(data)


def main():
    con = False
    print("Starting server 1...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    while not con:
        try:
            server.connect((IP, 6003))
            print("Connection to server 3 sucessfull")
            con = True
        except:
            print("...", end="")

    while True:
        time.sleep(5)
        thread = threading.Thread(target=GerarSend, args=(server,))
        thread.start()


if __name__ == "__main__":
    main()
