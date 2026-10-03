import socket

HOST = "127.0.0.1"
PORT = 5000

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server started...")
print(f"Listening on {HOST}:{PORT}")

conn, address = server_socket.accept()
print("Connected by:", address)

message = conn.recv(1024).decode()
print("Message received from client:", message)

response = "Message received successfully by server."
conn.send(response.encode())

conn.close()
server_socket.close()

print("Server connection closed.")
