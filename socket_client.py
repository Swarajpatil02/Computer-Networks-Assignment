import socket

HOST = "127.0.0.1"
PORT = 5000

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

message = input("Enter message to send to server: ")
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print("Response from server:", response)

client_socket.close()
print("Client connection closed.")
