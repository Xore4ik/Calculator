import socket




_HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
_PORT = 9000  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((_HOST, _PORT))
    sock.listen(1)

    conn, addr = sock.accept()

    with conn:
        print(f"Conected with {addr}")
        
        while True:
            data = conn.recv(1)

            if not data: break

            conn.send(data)