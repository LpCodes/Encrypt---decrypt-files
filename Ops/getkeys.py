"""
    Author  -  Lovelesh Pandey
    Created - 18-Jan-24
    Contact -  lovelesh_p@outlook.com
"""
import os
from pathlib import Path

from cryptography.fernet import Fernet

keys_path = Path(os.path.join(os.getcwd(), 'keys', 'key.key'))


def write_key():
    """
    Generates a key and save it into a file
    The Fernet.generate_key() function generates a fresh fernet key,
    you really need to keep this in a safe place. If you lose the key,
    you will no longer be able to decrypt data that was encrypted with this key.
    """
    key = Fernet.generate_key()

    with open(keys_path, "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open(keys_path, "rb").read()


if __name__ == '__main__':
    write_key()
    key = load_key()
    print(key)
