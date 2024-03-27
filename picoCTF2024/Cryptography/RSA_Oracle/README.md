# rsa_oracle
Can you abuse the oracle?
An attacker was able to intercept communications between a bank and a fintech company. They managed to get the [message](https://artifacts.picoctf.net/c_titan/33/secret.enc) (ciphertext) and the [password](https://artifacts.picoctf.net/c_titan/33/password.enc) that was used to encrypt the message.

After some intensive reconassainance they found out that the bank has an oracle that was used to encrypt the password and can be found here nc titan.picoctf.net 52816. Decrypt the password and use it to decrypt the message. The oracle can decrypt anything except the password.

## Solution
The Oracle allows for encryption of all messages, and decryption of all messages except for the password. This is not problem, due to the multiplicatory property of RSA.

The steps to solve the challenge are:

1. Send the encoded number 2 as a hexadecimal byte to the oracle. It is important that this value is equal to 0x02. The number "2" will be equal to "32" in HEX. This is why the following command is used: `io.sendline(b"e\n\x02")`.
2. Multiply the encoded value of 0x02 with the password. This gives us the product of the two encrypted messages.
3. Decrypt the product using the Oracle. This will leave us with a relatively small message. 
4. Convert the output from HEX to decimal, and divide it by 2 (the number we chose in the beginning). This will leave us with the password, once we convert it to text.
5. Decrypt the file using openssl and the password.

Here is my script to better explain the process:

```python
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
```

picoCTF{su((3ss_(r@ck1ng_r3@_4955eb5d}