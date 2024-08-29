from cryptography.fernet import Fernet

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

def generate_key():
    return Fernet.generate_key().decode()  # Generate a proper 32-byte key
