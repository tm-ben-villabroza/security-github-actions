import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv


load_dotenv()
key = bytes(os.getenv('KEY'), "utf-8")
f = Fernet(key)

token = f.encrypt(b"A really secret message. Not for prying eyes.")
print(token)

msg = f.decrypt(token)
print(msg)