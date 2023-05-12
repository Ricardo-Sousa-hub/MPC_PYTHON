import socket
import threading
import random as r
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 8003
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "3"

maior = "1"
menor = "2"

sr1Con = False
sr2Con = False
clientCon = False

MIN = 1
MAX = 100

k = "null"


def main():
    print("[STARTING] Server 3 is starting ...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server 3 is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_con, args=(conn, addr))
        thread.start()


def handle_con(conn, addr):
    print("NEW CONNECTION")

    confirmCon(conn, addr)

    conn.close()


def confirmCon(conn, addr):
    global clientCon
    global sr1Con
    global sr2Con
    if addr[1] == 8000:
        clientCon = True
        print("Connected to client!")
        client(conn, addr)
    if addr[1] == 8001:
        sr1Con = True
        print("Connected to Server 1!")
        server1(conn, addr)
    if addr[1] == 8002:
        sr2Con = True
        print("Connected to Server 2!")
        server2(conn, addr)


def client(conn, addr):
    global k
    global clientCon
    global sr1Con
    global sr2Con
    while clientCon and addr[1] == 8000:  # conexão bem sucedida com o cliente
        op = conn.recv(SIZE).decode(FORMAT)
        if op == DISCONNECT_MSG:
            clientCon = False
            print("Client disconnected...")
        if (op == maior or op == menor) and addr[1] == 8000:
            if sr1Con and sr2Con:
                k = str(r.randint(MIN, MAX))
                print(f"K: {k}")
                print("=" * 20)
                clientCon = False
            else:
                conn.send(("Wait for server 1 and 2 to be connected").encode(FORMAT))


def server1(conn, addr):
    global k
    global sr1Con
    global clientCon
    while sr1Con and addr[1] == 8001:  # sr2Con
        if sr1Con and k != "null":
            print("K sended to server 1")
            conn.send(k.encode(FORMAT))
            print("Server 1 disconnected...")
            sr1Con = False
            k = "null"


def server2(conn, addr):
    global k
    global sr2Con
    while sr2Con and addr[1] == 8002:  # sr1Con
        if sr2Con and k != "null":
            print("K sended to server 2")
            conn.send(k.encode(FORMAT))
            print("Server 2 disconnected...")
            sr2Con = False
            k = "null"


if __name__ == "__main__":
    main()
