# No need for Brutus
A simple message for you to decipher:

squiqhyiiycfbudeduutvehrhkjki

Submit the original plaintext hashed with MD5, wrapped between the usual flag format: flag{}

Ex: If the deciphered text is "hello world", the MD5 hash would be 5eb63bbbe01eeed093cb22bb8f5acdc3, and the flag would be flag{5eb63bbbe01eeed093cb22bb8f5acdc3}.

## Solution

Googled "Brutus" and found Caesar cipher. Bruteforced it using [dcode.fr](https://www.dcode.fr/caesar-cipher) and got the correct string. Then, I turned it into MD5 and delivered the flag.