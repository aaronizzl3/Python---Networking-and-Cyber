import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 65432

sock.bind((host, port))

while True:
    sock.listen(1)

    conn, addr = sock.accept()

    with conn:
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)