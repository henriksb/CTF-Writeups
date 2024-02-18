def enc1(data, param_2):
    # Convert the input string to a mutable byte array for XOR operation
    encrypted_data = bytearray(data, 'utf-8')
    
    # Perform the XOR operation for the first 24 bytes or the length of the data, whichever is smaller
    for i in range(min(24, len(encrypted_data))):
        encrypted_data[i] ^= param_2
    
    # Return the resulting encrypted data as a byte array
    return encrypted_data

# Example usage
enc_flag = 'lPmqXZR\v\rBJ\bMQfQ\tUVZK\tWD'  # This should be set to the expected value
dec_flag = enc1(enc_flag, ord('9'))
print(dec_flag)
