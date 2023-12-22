import socket
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "3"
ADDR_SERVER3 = (IP, 8003)
ADDR_SERVER4 = (IP, 8004)

x = "null"
y = "null"

# server1 = "x"
# server2 = "y"
connected = False
conS1 = False
conS2 = False
conS4 = False


def escreverMenu():
    print("1 - >")
    print("2 - <")
    print("3 - Disconnect")


def resultado(op, res):
    if op == 1:
        if "<" in res:
            resultado1 = res.split("<")
            final = resultado1[1] + " > " + resultado1[0]
            return final
        else:
            return res
    else:
        if ">" in res:
            resultado1 = res.split(">")
            final = resultado1[1] + " < " + resultado1[0]
            return final
        else:
            return res


def main():
    executing = True
    global conS1
    global conS2
    global conS4
    global connected
    global y
    op = ""
    while executing:
        conS1 = False
        conS2 = False
        conS4 = False
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
                    if msg == "Wait for server 4 to be connected":
                        print(msg)
                    else:
                        client.send(DISCONNECT_MSG.encode(FORMAT))
                        client.close()

                        connected = False

        if executing:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.bind(ADDR)

            #receber resultado do servidor 4

            while not conS4:
                try:
                    client.connect(ADDR_SERVER4)
                    if not conS4:
                        conS4 = True
                except:
                    print("Trying to connect to server 4")
                    time.sleep(5)
            print("Connected to server 4")
            while conS4:
                msg = client.recv(SIZE).decode(FORMAT)
                print(resultado(op, msg))
                conS4 = False


if __name__ == "__main__":
    main()
