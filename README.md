# -IMPLEMENTING-CRYPTOSYSTEMS
# Cryptosystem Project

## Overview
The Cryptosystem project is a Python implementation of three cryptographic algorithms: Caesar Cipher, RSA Encryption, and Baconian Cipher. Additionally, it includes a secure key exchange mechanism using primitive roots and the Diffie-Hellman key exchange algorithm.

## Table of Contents
1. [Installation]
2. [Usage]
3. [Files]
4. [Cryptographic Algorithms]
    - [Caesar Cipher]
    - [RSA Encryption]
    - [Baconian Cipher]
5. [Diffie-Hellman Key Exchange]
    - [Overview]
    - [Steps]
6. [Project Structure]
7. [Conclusion]

## Installation
1. Clone the repository: git clone https://github.com/your_username/cryptosystem.git
2. Navigate to the project directory: cd cryptosystem
3. Install required dependencies: pip install pycryptodome

## Usage 
1. Run the server: python server.py
2. Run the client: python client.py
    - Enter a prime number (p) when prompted.
3. Run the cryptosystem: python cryptosystem.py
    - Choose a cipher (1 for Caesar, 2 for RSA, 3 for Baconian) or exit (4).

## Files 
1. *cryptosystem.py*: Implementation of cryptographic algorithms (Caesar, RSA, Baconian) and the main menu for user interaction.
2. *client.py*: Client side of the Diffie-Hellman key exchange. Generates a private key, exchanges public keys, and calculates the shared secret key.
3. *server.py*: Server side of the Diffie-Hellman key exchange. Generates a private key, listens for incoming connections, and exchanges public keys.

## Cryptographic Algorithms 

### 1. Caesar Cipher
- *Functionality*: Encrypts and decrypts text using a simple shift-based substitution method.
- **Usage in cryptosystem.py**: User can input text and a shift value to encrypt and decrypt messages.

### 2. RSA Encryption
- *Functionality*: Generates public and private key pairs for encryption and decryption using the RSA algorithm.
- **Usage in cryptosystem.py**: User can input a message, and the program generates public and private keys, encrypts and decrypts the message using RSA.

### 3. Baconian Cipher
- *Functionality*: Encrypts and decrypts text using a binary representation of characters with 'A' and 'B'.
- **Usage in cryptosystem.py**: User can input text to be encrypted and decrypted using the Baconian Cipher.

## Diffie-Hellman Key Exchange <a name="diffie-hellman-key-exchange"></a>

### Overview
The Diffie-Hellman key exchange is implemented in the client.py and server.py files to securely exchange keys over an insecure channel.

### Steps 
1. **Server Side (server.py)**:
    - Generates a private key (a) and a primitive root (g).
    - Listens for incoming connections.
    - Sends the public key (g^a mod p) to the client.

2. **Client Side (client.py)**:
    - Generates a private key (b) and a primitive root (g).
    - Establishes a connection with the server.
    - Receives the server's public key (g^a mod p).
    - Sends the client's public key (g^b mod p) to the server.
    - Calculates the shared secret key (g^(ab) mod p).

## Project Structure 
- cryptosystem/
    - cryptosystem.py
    - client.py
    - server.py

## Conclusion 
The Cryptosystem project demonstrates the implementation of various cryptographic algorithms and a secure key exchange mechanism. It serves as an educational tool for understanding cryptography basics, key exchange, and the practical use of different ciphers.
