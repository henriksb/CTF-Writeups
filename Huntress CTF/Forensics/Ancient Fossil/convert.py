import base64

with open("output", "r") as file:
    for line in file.readlines()[1:-2]:
        print(base64.b64decode(line.split()[2]).decode(), end="")
