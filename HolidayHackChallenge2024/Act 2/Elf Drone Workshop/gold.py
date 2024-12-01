def binary_to_text(binary_string):
    # Convert the binary string to ASCII
    return ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8) if len(binary_string[i:i+8]) == 8)

final_string = ""

with open("ELF-HAWK-dump.csv", "r") as csv:
    for line in csv:
        # Replace TRUE/FALSE with binary and concatenate
        binary_string = ''.join('1' if value == "TRUE" else '0' for value in line.split(",") if value in {"TRUE", "FALSE"})
        
        # Skip lines with no binary data
        if '1' in binary_string:
            final_string += binary_string

print(binary_to_text(final_string))
