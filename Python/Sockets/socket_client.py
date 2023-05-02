import socket

IP = socket.gethostbyname(socket.gethostname())
PORT =5568
ADDR=(IP,PORT)
SIZE=1024
FORMAT="utf-8"
DISCONNECT_MSG="Disconnected!"

def main():
    #print("[STARTING] Server is starting ...")
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to Server at {IP}:{PORT}")
    connected=True
    while connected:
        msg = input(">")
        client.send(msg.encode(FORMAT))
        if msg== DISCONNECT_MSG:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")


    #server.bind(ADDR)
    #server.listen()
    #print(f"[LISTENING] Server is listening on {IP}")

if __name__ == "__main__":
    main()