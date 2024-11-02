# Base-p-
That looks like a weird encoding, I wonder what it's based on.

## Solution
The title was a pretty obvious hint that this file was encoded using a different base. Considering that I only saw Chinese characters in the file, I assumed the base was fairly high. When using base bruteforcers online I got no results. After a little while I came across `base65536`, which was correct.

I found a python module to decode the data:

```python
import base65536

with open('based.txt', 'r', encoding="utf-8") as f:
    ct = f.readline().rstrip().replace(' ', '')

compressed_data = base65536.decode(ct)

>> b'H4sIAG0OA2cA/+2QvUt6URjHj0XmC5ribzBLCwKdorJoSiu9qRfCl4jeILSICh1MapCINHEJpaLJVIqwTRC8DQ5BBQ0pKtXUpTej4C4lBckvsCHP6U9oadDhfL7P85zzPTx81416LYclYgEAOLgOGwKgxgnrJKMK8j4kIaAwF3TjiwCwBejQQDAshK82cKx/2BnO3xzhmEmoMWn/qdU+ntTUIO8gmOw438bbCwRv3Y8vE2ens9y5sejat497l51sTRO18E8j2aSAAkixqhrKFl8E6fZfotmMlw7Z3NKFmvp92s8+HMg+zTwaycvVQlnSn7FYW2LFYY0+X18JpB9LCYliSm6LO9QXvfaIbJAqvNsL3lTP6vJ596GyKIaXBnNdRJahnqYLnlQ4d+LfbQ91vpH0Y4NSYwhk8tmv/5vFZFnHWrH8qWUkTfgfUPXKcFVi+5Vlx7V90OjLjZqtqMMH9FhMZfGUALnotancBQAA'
```
The result was clearly gzip compressed data, which when decoded turned into an image:

```python
import gzip
import base64

decoded_compressed_data = base64.b64decode(compressed_data)

decompressed_data = gzip.decompress(decoded_compressed_data)

with open('decompressed_file_out.png', 'wb') as f3:
    f3.write(decompressed_data)
```
![alt text](decompressed_file_out.png)

This last step had me stuck for a while. I though about decoding the HEX values of each color, but somehow got the values wrong which led me into a big rabbit hole. I told my teammate what I had done, and he did the same, but with a different website and got the flag..

```python
import binascii
hex_string = "666c61677b35383663663863383439633937333065613762323131326666663339666636617d20"

print(binascii.unhexlify(hex_string).decode())
```

