import random
from Crypto.Util.number import bytes_to_long, long_to_bytes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, t1, t2 = m, 0, 1
    while a > 1:
        q = m // a  # Calculate the quotient
        m, a = a, m % a  # Update m and a based on the remainder
        t1, t2 = t2, t1 - q * t2  # Update t1 and t2
    return t2 + m0 if t2 < 0 else t2

def generate_prime():
    while True:
        candidate = random.randint(100, 100000000)
        if is_prime(candidate):
            return candidate

def generate_key_pair():
    p = generate_prime()
    q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

def encrypt_rsa(message, public_key):
    n, e = public_key
    message_bytes = message.encode('utf-8')
    message_int = bytes_to_long(message_bytes)
    encrypted_message = pow(message_int, e, n)
    return encrypted_message

def decrypt_rsa(ciphertext, private_key):
    n, d = private_key
    decrypted_message_int = pow(ciphertext, d, n)
    decrypted_message_bytes = long_to_bytes(decrypted_message_int)
    decrypted_message = decrypted_message_bytes.decode('utf-8')
    return decrypted_message

def baconian_encrypt(plaintext):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            binary_representation = bin(ord(char) - ord('A'))[2:].zfill(5) if char.isupper() else bin(ord(char) - ord('a'))[2:].zfill(5)
            ciphertext += binary_representation.replace('0', 'A').replace('1', 'B')
        else:
            ciphertext += char
    return ciphertext

def baconian_decrypt(ciphertext):
    ciphertext=ciphertext.replace(" ","     ")
    plaintext = ''
    for i in range(0, len(ciphertext), 5):
        group = ciphertext[i:i+5]
        binary_representation = group.replace('A', '0').replace('B', '1')
        try:
            decimal_value = int(binary_representation, 2)
            if 0 <= decimal_value <= 25:
                plaintext += chr(decimal_value + ord('A'))
            elif 26 <= decimal_value <= 51:
                plaintext += chr(decimal_value + ord('a') - 26)
            else:
                plaintext += group
        except ValueError:
            plaintext += group
    return plaintext.replace("     "," ")

def main():
    print("WELCOME")
    while True:
        print("Choose the Cipher you want")
        print("1. Caesar Cipher")
        print("2. RSA Encryption")
        print("3. Baconian Cipher")
        print("4. Exit")
        choice = int(input("Choose a cipher (1, 2, 3, or 4 to exit): "))

        if choice == 1:
            plaintext = input("Enter text: ")
            shift = int(input("Enter shift: "))
            encrypted_text = encrypt_caesar(plaintext, shift)
            decrypted_text = decrypt_caesar(encrypted_text, shift)
            print(f"Encrypted: {encrypted_text}")
            print(f"Decrypted: {decrypted_text}")
        elif choice == 2:
            message = input("Enter message: ")
            public_key, private_key = generate_key_pair()
            encrypted_message = encrypt_rsa(message, public_key)
            decrypted_message = decrypt_rsa(encrypted_message, private_key)
            print(f"Public Key: {public_key}")
            print(f"Private Key: {private_key}")
            print(f"Encrypted Message: {encrypted_message}")
            print(f"Decrypted Message: {decrypted_message}")
        elif choice == 3:
            plaintext = input("Enter text: ")
            encrypted_text = baconian_encrypt(plaintext)
            decrypted_text = baconian_decrypt(encrypted_text)
            print(f"Encrypted: {encrypted_text}")
            print(f"Decrypted: {decrypted_text}")
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
main()


