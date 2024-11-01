import socket, re

s = socket.create_connection(('challenge.ctf.games', 30463))
ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
buffer = ""

while (data := s.recv(1024).decode('utf-8')):
    buffer += data
    clean_data = ansi_escape.sub('', buffer)
    if "flag{" in clean_data and "}" in clean_data:
        print(clean_data[clean_data.index("flag{"):clean_data.index("}")+1])
        break
