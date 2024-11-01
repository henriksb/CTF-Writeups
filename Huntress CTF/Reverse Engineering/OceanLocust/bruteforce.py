import subprocess
import os
import struct

# Function to extract and print chunks from a PNG file, returning a one-dimensional list of bytes
def extract_png_chunks(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist!")
    
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
            
            # Convert chunk type to string
            chunk_type = chunk_type.decode("ascii")
            
            if chunk_type.startswith("biT"):  # Check if chunk type starts with "biT"
                # Convert the chunk data into a list of individual bytes in hexadecimal
                chunk_data_list = [f"{byte:02x}" for byte in chunk_data]
                chunks.append((chunk_type, chunk_data_list))  # Store both type and data
    
    # Sort the chunks based on the chunk type (e.g., 'biTa', 'biTb', etc.)
    sorted_chunks = sorted(chunks, key=lambda x: x[0])

    # Flatten the sorted list into one-dimensional byte list
    flattened_bytes = [byte for _, chunk_data in sorted_chunks for byte in chunk_data]

    return flattened_bytes

# Function to encode the flag into a PNG
def encode_png_with_flag(flag_guess):
    # Pass the command as a list of arguments to avoid shell issues with special characters
    command = ["./png-challenge.exe", "bilde.png", flag_guess]
    subprocess.run(command, check=True)  # No need for shell=True here

# Function to extract chunks from the PNG and return a list of bytes
def extract_chunks():
    return extract_png_chunks('./encoded bilde.png')

# Function to compare the extracted bytes with the correct sequence
def compare_bytes(extracted_bytes, correct_bytes):
    return extracted_bytes[:len(correct_bytes)] == correct_bytes

# Brute-force the flag byte-by-byte
def brute_force_flag():
    # Correct byte sequence (known from your task)
    correct_bytes = ['04', '05', '35', '06', '19', '04', '0c', '37', '5a', '55', '01', '5f', '6d', '53', '00', 
                     '5a', '0c', '37', '5c', '06', '54', '5c', '36', '5d', '00', '00', '58', '64', '03', '07', 
                     '55', '0b', '36', '51', '57', '06', '59', '29', 'c2', 'c8']
    
    # Start with 40 '0's as the initial flag guess
    flag_guess = "0" * 40
    flag_list = list(flag_guess)

    # Loop over each byte position (0 to 39)
    for byte_position in range(40):
        for ascii_char in range(32, 127):  # Try all printable ASCII characters
            # Set the current byte in the flag guess
            flag_list[byte_position] = chr(ascii_char)
            current_flag_guess = ''.join(flag_list)

            # Encode the PNG with the current flag guess
            encode_png_with_flag(current_flag_guess)

            # Extract the bytes from the encoded file
            extracted_bytes = extract_chunks()

            # Compare the extracted bytes with the correct byte sequence
            if compare_bytes(extracted_bytes, correct_bytes[:byte_position + 1]):
                print(f"Matched byte {byte_position + 1}: {current_flag_guess}")
                break  # Move to the next byte after a match

    # Final flag result
    final_flag = ''.join(flag_list)
    print(f"Final flag: {final_flag}")

# Run the brute-force flag finder
if __name__ == "__main__":
    brute_force_flag()
