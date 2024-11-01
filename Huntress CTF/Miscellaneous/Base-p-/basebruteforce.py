import gzip
import base64
import binascii
import base65536


def part1():
    with open('based.txt', 'r', encoding="utf-8") as f:
        ct = f.readline().rstrip().replace(' ', '')

    with open('FILE_out', 'wb') as f2:
        f2.write(base65536.decode(ct))

    compressed_data = 'H4sIAG0OA2cA/+2QvUt6URjHj0XmC5ribzBLCwKdorJoSiu9qRfCl4jeILSICh1MapCINHEJpaLJVIqwTRC8DQ5BBQ0pKtXUpTej4C4lBckvsCHP6U9oadDhfL7P85zzPTx81416LYclYgEAOLgOGwKgxgnrJKMK8j4kIaAwF3TjiwCwBejQQDAshK82cKx/2BnO3xzhmEmoMWn/qdU+ntTUIO8gmOw438bbCwRv3Y8vE2ens9y5sejat497l51sTRO18E8j2aSAAkixqhrKFl8E6fZfotmMlw7Z3NKFmvp92s8+HMg+zTwaycvVQlnSn7FYW2LFYY0+X18JpB9LCYliSm6LO9QXvfaIbJAqvNsL3lTP6vJ596GyKIaXBnNdRJahnqYLnlQ4d+LfbQ91vpH0Y4NSYwhk8tmv/5vFZFnHWrH8qWUkTfgfUPXKcFVi+5Vlx7V90OjLjZqtqMMH9FhMZfGUALnotancBQAA'

    decoded_compressed_data = base64.b64decode(compressed_data)

    decompressed_data = gzip.decompress(decoded_compressed_data)

    with open('decompressed_file_out.png', 'wb') as f3:
        f3.write(decompressed_data)

# Color HEX values
hex_string = "666c61677b35383663663863383439633937333065613762323131326666663339666636617d20"

print(binascii.unhexlify(hex_string).decode())
