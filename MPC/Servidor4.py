import socket
import threading
import time
import random as r

IP = socket.gethostbyname(socket.gethostname())
PORT = 8004
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "3"

ADDR_SERVER1 = (IP, 8001)
ADDR_SERVER2 = (IP, 8002)
ADDR_CLIENT = (IP, 8000)

x = "null"
y = "null"

conS1 = False
conS2 = False
clientCon = False


def analisarInput(x, y):
        if len(x) > len(y):
            return "Server 1(X) > Server 2(Y)"
        if len(x) < len(y):
            return "Server 2(Y) > Server 1(X)"
        if len(x) == len(y):
            if x == y:
                return "Server 1(x) = Server 2(y)"
            index = 2
            for i in range(2, len(x)-1):
                if int(x[i]) > int(y[index]):
                    return "Server 1(X) > Server 2(Y)"
                if int(x[i]) < int(y[index]):
                    return "Server 2(Y) > Server 1(X)"
                index += 1


def handle_conS1(conn):
    global conS1
    global x
    print("A receber X!")
    while not conS1:
        x = conn.recv(SIZE).decode(FORMAT)
        print(f"X: {x}")
        if x != "null" and x != "":
            conn.close()
            conS1 = True


def handle_conS2(conn):
    global conS2
    global y
    print("A receber Y!")
    while not conS2:
        y = conn.recv(SIZE).decode(FORMAT)
        print(f"Y: {y}")
        if y != "null" and y != "":
            conn.close()
            conS2 = True


def handle_conClient(conn):
    global x
    global y
    global conS1
    global conS2
    global clientCon
    while not clientCon:
        if conS1 and conS2 and not clientCon:
            resultado = analisarInput(x, y)
            if not resultado.isspace() and resultado != "":
                print(resultado)
                conn.send(resultado.encode(FORMAT))
                conn.close()
                clientCon = True


def handle_con(conn, addr):
    if addr[1] == 8001:
        handle_conS1(conn)
    if addr[1] == 8002:
        handle_conS2(conn)
    if addr[1] == 8000:
        handle_conClient(conn)


def main():
    global conS1
    global conS2
    global clientCon
    global x
    global y
    executing = True
    while executing:
        conS1 = False
        conS2 = False
        clientCon = False
        print("[STARTING] Server 4 is starting ...")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        print("Trying to connect to server 1 and server 2")
        server.listen()

        #thread = threading.Thread(target=handle_con, args=(conn, addr))
        #thread.start()

        while not conS1 or not conS2 or not clientCon:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_con, args=(conn, addr))
            thread.start()

        print("END")


if __name__ == "__main__":
    main()
