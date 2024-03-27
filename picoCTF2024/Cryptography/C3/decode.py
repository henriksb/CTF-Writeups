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

