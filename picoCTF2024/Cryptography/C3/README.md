# C3
This is the Custom Cyclical Cipher!

Download the ciphertext [here](https://artifacts.picoctf.net/c_titan/47/ciphertext).
Download the encoder [here](https://artifacts.picoctf.net/c_titan/47/convert.py).

Enclose the flag in our wrapper for submission. If the flag was "example" you would submit "picoCTF{example}".

## Solution
In this challenge, we receive a Python script that has been used to encode a file. We have also received the encoded file, which we have to decrypt. This is the decoding script we received:

```python
import sys
chars = ""
from fileinput import input
for line in input():
  chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
  cur = lookup1.index(char)
  out += lookup2[(cur - prev) % 40]
  prev = cur

sys.stdout.write(out)
```

We then have to reverse the processes of this script, and use this on the encrypted file. I created the following script for this job:

```python
# The lookup strings
lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

def decrypt_text(encoded_chars):
    decoded_out = ""
    prev = 0

    for char in encoded_chars:
        if char in lookup2:  # Make sure the character is in lookup2
            cur_encoded_index = lookup2.index(char)
            cur_original_index = (prev + cur_encoded_index) % len(lookup1)
            decoded_char = lookup1[cur_original_index]
            decoded_out += decoded_char
            prev = cur_original_index
        else:
            decoded_out += char  # If char not in lookup2, keep it as is

    return decoded_out

# Read the content of the file named "ciphertext"
with open("ciphertext", "r") as file:
    encoded_text = file.read()

# Decrypt the content
decrypted_text = decrypt_text(encoded_text)

print(decrypted_text)
```
This produces another python script:

```python
#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1
```

To get the flag, run the new script on itself: `python2 output.py output.py`. This gives the output: "adlibs".

picoctf{adlibs}