import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 8003
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "3"
client_addr = (IP, 8000)


def escreverMenu():
    print("1 - >=")
    print("2 - <=")
    print("3 - Disconnect")


def main():
    connected = False
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.bind(client_addr)
    while not connected:
        try:
            client.connect(ADDR)
            if not connected:
                connected = True
        except:
            print("Trying to connect to server 3")
    print(f"[CONNECTED] Client connected to Server at {IP}:{PORT}")
    connected=True
    while connected:
        escreverMenu()
        op = input("-> ")

        if not op.isnumeric() or int(op) > 3 or int(op) < 1:
            print("Digite uma opcao valida!")
        else:
            client.send(op.encode(FORMAT))
            if op == DISCONNECT_MSG:
                connected = False
            else:
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}")


if __name__ == "__main__":
    main()
