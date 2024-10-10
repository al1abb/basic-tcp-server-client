import socket, threading, sys

IP = "192.168.30.20"
PORT = int(sys.argv[1])

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((IP, PORT))
tcp_server.listen(5)
print(f"[*] Listening on {IP}:{PORT}")

def handle_client(client_socket):
    with client_socket as sock:
        while True:
            request = sock.recv(1024)
            if not request:
                print("[*] Client disconnected.")
                break
            print(f"[*] {request.decode('utf-8')}")
            sock.send(b"ACK")

while True:
    client, address = tcp_server.accept()
    print(f"[*] Accepted connection from {address[0]}:{address[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()