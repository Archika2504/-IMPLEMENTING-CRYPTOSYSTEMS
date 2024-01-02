import socket
import random

# Get prime number and primitive root from user
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))

# Client's private key
b = random.randint(1, p-1)

client_socket = socket.socket()
client_socket.connect(('localhost', 12345))  # Replace with server's IP and port

# Receive server's public key (g^a mod p)
server_public_key = int(client_socket.recv(1024).decode('utf-8'))

# Send client's public key (g^b mod p) to server
client_socket.sendall(bytes(str(pow(g, b, p)), 'utf-8'))

# Calculate shared secret key (g^ab mod p)
shared_secret_key = pow(server_public_key, b, p)
print("Shared secret key:", shared_secret_key)

client_socket.close()
