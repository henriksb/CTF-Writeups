import struct
import sys

# Function to extract and print chunks from a PNG file
def extract_png_chunks(file_path):
    chunks = []
    with open(file_path, "rb") as f:
        # Skip the PNG signature (first 8 bytes)
        f.read(8)
        while True:
            # Read the length (4 bytes) and the chunk type (4 bytes)
            data = f.read(8)
            if len(data) < 8:
                break  # End of file
            length, chunk_type = struct.unpack(">I4s", data)
            chunk_data = f.read(length)  # Read the chunk data
            f.read(4)  # Skip the CRC
            chunk_type = chunk_type.decode("ascii")
            if chunk_type.startswith("biT"):  # Check if chunk type starts with "biT"
                chunks.append((chunk_type, chunk_data))
    return chunks

# Extract and display the chunks that start with "biT"
png_chunks = extract_png_chunks(sys.argv[1])
print(sorted(png_chunks))


# a = 0x03
# b = 0x00
# c = 0x01
# d = 0x06
# e = 0x07
# f = \x04

# h = \n

"""
[('biTg', b'\x03\x04'), ('biTb', b'\x0b\x1a'), ('biTi', b'\x0c\xc3'), ('biTa', b'\n\x0c'), 
('biTe', b'\x0e\x05'), ('biTd', b'\x0c\x08'), ('biTc', b'\x03\x07'), ('biTh', b'\x0f\x0c'), 
('biTf', b'\x07\x1a')]


('biTa', b'\x04\x055 \x06 \x19')
('biTb', b'\x04\x0c7 Z U')
('biTc', b'\x01_m S\x00')
('biTd', b'Z\x0c7 \\ \x06')
('biTe', b'T\\6 ] \x00')
('biTf', b'\x00Xd \x03 \x07'),
('biTg', b'U\x0b6 QW')]
('biTh', b'\x06Y) \xc2\xc8'), 
 

ffc86b7dgn=g>:i; WU  T TK d81>?a3  {7bdbe5 

"""