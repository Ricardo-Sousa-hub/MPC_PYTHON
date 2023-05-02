# Server 3

import socket
import threading

ip = socket.gethostbyname(socket.gethostname())
port = 6003
ADDR = (ip, port)
size = 1024
format = "utf-8"
deconn = "Disconnected!"
connected = True


def handle_client(conn, addr):
    print(f"[NEW CONNECTION]")
    connected = True
    while connected:
        msg = conn.recv(size).decode(format)
        if msg == deconn:
            connected = False
        print(f"[{addr}]{msg}")
        msg = f"Msg received: {msg}"
        conn.send(msg.encode(format))

    conn.close()


def main():
    print("[STARTING] Server is starting ...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {ip}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    main()
