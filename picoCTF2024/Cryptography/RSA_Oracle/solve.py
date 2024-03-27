import subprocess
from pwn import *

ENCRYPTED_PASSWORD = 1634668422544022562287275254811184478161245548888973650857381112077711852144181630709254123963471597994127621183174673720047559236204808750789430675058597

# Establish a connection to the RSA oracle.
# The oracle provides an encryption/decryption service vulnerable to chosen plaintext attacks.
io = remote("titan.picoctf.net", 52816)

# Send the encoded number 2 as a hexadecimal byte to the oracle.
# This step is crucial for the chosen plaintext attack, where we need the oracle's encrypted response for 2.
io.sendline(b"e\n\x02")

output = io.recvuntil(b"ciphertext (m ^ e mod n)")
encrypted_number = int(io.recvline().strip().decode())

# Multiply our password with the known message.
# This exploits RSA's multiplicative property: (m1 * m2) mod n = (c1 * c2) mod n,
# where m1 and m2 are plaintext messages, and c1 and c2 are their corresponding ciphertexts.
product = ENCRYPTED_PASSWORD*encrypted_number

# Request the oracle to decrypt the product of the encrypted password and the encrypted number 2.
# This manipulation allows us to indirectly learn about the plaintext of the encrypted password.
io.sendline(b"d")
io.sendline(str(product).encode())

io.recvuntil(b"decrypted ciphertext as hex (c ^ d mod n):")
decrypted_number = io.recvline().strip().decode()

# Fix format and divide by the number from our first message (2) to get the password
password = hex(int(decrypted_number, 16)//2)

# Turn HEX into text and remove "0x". This is the password.
password = bytes.fromhex(password[2:]).decode("utf-8")
print("Password: " + password)

# Decrypt and print the flag.
print("\n")
subprocess.run(['openssl', 'enc', '-aes-256-cbc', '-d', '-in', 'secret.enc','-k', password], check=True)
print("\n")



