from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Correct 32-byte key
key = b'Sixteen byte keySixteen byte key'

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv + ct

def decrypt_message(enc_message):
    iv = base64.b64decode(enc_message[:24])
    ct = base64.b64decode(enc_message[24:])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')
