import socket
import threading
import random as r

IP = socket.gethostbyname(socket.gethostname())
PORT = 8003
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "3"
maior = "1"
menor = "2"
sr1 = False
sr2 = False
k = 0
executed = False


def gerarNumero():
    return r.randint(1, 101)


def sendToServer(k, addr, conn):
    server = ""
    if addr == 8001:
        server = "Server 1\n"
    if addr == 8002:
        server = "Server 2\n"

    conn.send(str(k).encode(FORMAT))
    print(f"K sended to {server}")
    msg = conn.recv(SIZE).decode(FORMAT)
    print(msg)
    main()


def confirmCon(addr):
    global sr1
    global sr2
    if addr[1] == 8000:
        print("Connected to client!")

    if addr[1] == 8001:
        sr1 = True
        print("Connected to Server 1!")

    if addr[1] == 8002:
        sr2 = True
        print("Connected to Server 2!")


def handle_client(conn, addr):
    global k
    global executed
    print(f"[NEW CONNECTION]")
    connected = True

    confirmCon(addr)

    while connected and addr[1] == 8000:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False

        if (msg == maior or msg == menor) and addr[1] == 8000:
            k = gerarNumero()

        msg = f"Msg received: {msg}"
        conn.send(msg.encode(FORMAT))

    while connected and addr[1] == 8001 and not executed:
        if k != 0:
            conn.send(str(k).encode(FORMAT))
            print("K sended")
            msg = conn.recv(SIZE).decode(FORMAT)
            print(msg)
            executed = True

    while connected and addr[1] == 8002 and not executed:
        if k != 0:
            sendToServer(k, addr[1], conn)
            executed = True

    conn.close()


def main():
    print("[STARTING] Server is starting ...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    main()
