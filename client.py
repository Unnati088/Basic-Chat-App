
import socket

# Client setup
HOST = '127.0.0.1'  # Server IP
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"[CONNECTED] Connected to server at {HOST}:{PORT}")

while True:
    message = input("You: ")
    client_socket.send(message.encode())
    reply = client_socket.recv(1024).decode()
    if not reply:
        print("[DISCONNECTED] Server closed connection.")
        break
    print(f"Server: {reply}")

client_socket.close()
