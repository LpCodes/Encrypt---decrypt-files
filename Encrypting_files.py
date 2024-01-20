import os
from pathlib import Path

from cryptography.fernet import Fernet
from Ops.getkeys import load_key, write_key


def encrypt(filename, key):
    """
   Encrypts a file using Fernet symmetric encryption.

   Args:
       filename (str): The path to the file to encrypt.
       key (bytes): The Fernet encryption key.

   Raises:
       FileNotFoundError: If the specified file does not exist.
   """

    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    f = Fernet(key)

    with open(filename, "rb") as file:
        # Read the entire file contents into memory for encryption
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    # Overwrite the original file with the encrypted data
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
   Decrypts a file using Fernet symmetric encryption.

   Args:
       filename (str): The path to the file to decrypt.
       key (bytes): The Fernet encryption key.

   Raises:
       FileNotFoundError: If the specified file does not exist.
       cryptography.fernet.InvalidToken: If the file cannot be decrypted (e.g., wrong key or corrupt data).
   """

    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    f = Fernet(key)

    with open(filename, "rb") as file:
        # Read the encrypted file contents
        encrypted_data = file.read()
        print(encrypted_data)

    try:
        decrypted_data = f.decrypt(encrypted_data)
        print(decrypted_data)
        # Overwrite the encrypted file with the decrypted data
        with open(filename, "wb") as file:
            file.write(decrypted_data)

    except Exception as e:
        print(e)


# Generate and write a new key if needed
keys_path = Path(os.path.join(os.getcwd(), 'keys', 'key.key'))
if os.path.exists(keys_path):
    pass
else:
    write_key()

key = load_key()  # Load the existing key

# Example usage:
file_path = r"C:\Users\102\Downloads\log\Settings_preferences.xml"
# do encrypt or decrypt as required
# encrypt(file_path, key)  # Encrypt the file
decrypt(file_path, key)  # Decrypt the file
