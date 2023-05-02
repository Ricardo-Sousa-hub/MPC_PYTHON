import socket
import threading

# import wikipedia

IP = socket.gethostbyname(socket.gethostname())
PORT = 6003
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION]")
    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
        print(f"[{addr}]{msg}")
        msg = f"Msg received: {msg}"

        conn.send(msg.encode(FORMAT))
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