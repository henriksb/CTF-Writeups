# Sekiro Challenge

## Challenge Description
Connect to a container running a Sekiro-inspired game where you must counter enemy moves correctly.

## Game Mechanics
| Enemy Move | Required Counter |
|------------|-----------------|
| retreat    | strike         |
| strike     | block          |
| block      | advance        |
| advance    | retreat        |

## Solution
Game had 3 levels with increasing speed. Level 3 was impossible to beat manually due to timing constraints, requiring automation.

### Solution Script
```python
import socket
import time
import re

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

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
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
            
            lines = buffer.split("\n")
            buffer = lines.pop()
            
            for line in lines:
                match = re.search(r"Opponent move: (\w+)", line)
                if match:
                    opponent_move = match.group(1).strip()
                    counter_move = get_counter_move(opponent_move)
                    if counter_move:
                        time.sleep(0.5)
                        s.sendall((counter_move + "\n").encode('utf-8'))

if __name__ == "__main__":
    main()
```

## Flag
```
flag{a1ae4e5604576818132ce3bfebe95de5}
```
