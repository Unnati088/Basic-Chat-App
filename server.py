
import socket

# Server setup
HOST = '127.0.0.1'  # Localhost
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"[CONNECTED] Client connected from {addr}")

while True:
    message = conn.recv(1024).decode()
    if not message:
        print("[DISCONNECTED] Client closed connection.")
        break
    print(f"Client: {message}")
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()
server_socket.close()
