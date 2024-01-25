from Crypto.Cipher import AES
from base64 import b64decode
import json

def attempt_decryption(key, nonce, ciphertext, tag):
    try:
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return True, plaintext.decode('utf-8')
    except (ValueError, KeyError):
        return False, "Decryption failed"

hex_str1 = "a3c5a5a81ebc62c6144a9dc1ae5cce11"
hex_str2 = "980daad49738f76b80c8fafb0673ff1b"
hex_str3 = "fc78e6fee2138b798e1e51ed15e0a109"

key1 = bytes.fromhex(hex_str1)
key2 = bytes.fromhex(hex_str2)
key3 = bytes.fromhex(hex_str3)

with open("melding.enc", "rb") as f:
    data = json.loads(f.read())
    nonce = b64decode(data["nonce"])
    ciphertext = b64decode(data["ciphertext"])
    tag = b64decode(data["tag"])

key = bytes(a ^ b ^ c for a, b, c in zip(key1, key2, key3))

success, message = attempt_decryption(key, nonce, ciphertext, tag)
print(message)