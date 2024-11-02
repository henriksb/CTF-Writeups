import gzip
import base64
import binascii
import base65536


with open('based.txt', 'r', encoding="utf-8") as f:
    ct = f.readline().rstrip().replace(' ', '')

compressed_data = base65536.decode(ct)

decoded_compressed_data = base64.b64decode(compressed_data)

decompressed_data = gzip.decompress(decoded_compressed_data)

with open('decompressed_file_out.png', 'wb') as f3:
    f3.write(decompressed_data)


# Color HEX values
hex_string = "666c61677b35383663663863383439633937333065613762323131326666663339666636617d20"

print(binascii.unhexlify(hex_string).decode())
