import socket
import time
import re

# Define the correct responses
def get_counter_move(opponent_move):
    counter_moves = {
        "retreat": "strike",
        "strike": "block",
        "block": "advance",
        "advance": "retreat"
    }
    return counter_moves.get(opponent_move)

def main():
    host = "challenge.ctf.games"
    port = 32687

    # Connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Continuously read from the server and respond
        buffer = ""
        while True:
            try:
                data = s.recv(1024).decode('utf-8', errors='ignore')
            except UnicodeDecodeError:
                continue

            if not data:
                break

            buffer += data
            print(data)

            # Process lines from the buffer
            lines = buffer.split("\n")
            buffer = lines.pop()  # Keep the last incomplete line in the buffer

            for line in lines:
                # Look for the opponent's move
                match = re.search(r"Opponent move: (\w+)", line)
                if match:
                    opponent_move = match.group(1).strip()
                    counter_move = get_counter_move(opponent_move)

                    if counter_move:
                        # Send the counter move after a short delay
                        time.sleep(0.5)
                        s.sendall((counter_move + "\n").encode('utf-8'))

if __name__ == "__main__":
    main()