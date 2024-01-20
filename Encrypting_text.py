from cryptography.fernet import Fernet
from Ops.getkeys import load_key,write_key


def encrypt_message(message):
    """Encrypts a given message using Fernet."""

    key = load_key()  # Load the key once for efficiency
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())  # Use Encode as message is string t better efficiency within the function
    return encrypted


def decrypt_message(encrypted_message):
    """Decrypts a given encrypted message using Fernet."""

    key = load_key()  # Load the key once for efficiency
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message).decode()  # Decode within the function
    return decrypted


# Example usage:
message = "some random text"
write_key()
encrypted_data = encrypt_message(message)
print("Encrypted message:", encrypted_data)

decrypted_data = decrypt_message(encrypted_data)
print("Decrypted message:", decrypted_data)
