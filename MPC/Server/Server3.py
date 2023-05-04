import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 8003
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
server_status = False


def handle_other_server(conn, addr):
    print("New Connection...")
    connectedToServer1 = False
    connectedToServer2 = False
    if addr[1] == 8001:
        connectedToServer1 = True
        print("Connection to server 1 established...")
    if addr[1] == 8002:
        connectedToServer2 = True
        print("Connection to server 2 established...")

    while connectedToServer1 or connectedToServer2:
        if addr[1] == 8001:
            print(f"Server 1: {conn.recv(SIZE).decode(FORMAT)}")

        if addr[1] == 8002:
            print(f"Server 2: {conn.recv(SIZE).decode(FORMAT)}")


def main():
    print("Starting server 3...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    server_status = True
    print("Waiting for connections...")
    while server_status:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_other_server, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    main()
