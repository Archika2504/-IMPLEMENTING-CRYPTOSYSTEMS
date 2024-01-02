import socket
import random

# Get prime number and primitive root from user
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))

# Server's private key
a = random.randint(1, p-1)

server_socket = socket.socket()
server_socket.bind(('localhost', 12345))  # Replace with desired IP and port
server_socket.listen(1)

print("Server listening...")

client_socket, address = server_socket.accept()
print("Connected to client:", address)

# Send public key (g^a mod p) to client
client_socket.sendall(bytes(str(pow(g, a, p)), 'utf-8'))

# Receive client's public key (g^b mod p)
client_public_key = int(client_socket.recv(1024).decode('utf-8'))

# Calculate shared secret key (g^ab mod p)
shared_secret_key = pow(client_public_key, a, p)
print("Shared secret key:", shared_secret_key)

client_socket.close()
server_socket.close()
