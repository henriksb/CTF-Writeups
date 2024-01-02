def scytale_cipher_decode(text, diameter):
    circumference = len(text) // diameter

    decoded_message = ''
    for i in range(circumference):
        for j in range(i, len(text), circumference):
            decoded_message += text[j]

    return decoded_message


with open("melding.txt", 'r', encoding='utf-8') as f:
    f = f.read()

for i in range(1,100):
    scytale = scytale_cipher_decode(f, i)
    if scytale[0:4] == "pst{":
        print(scytale[0:scytale.find("}")+1])
        print("Diameter: " + str(i))