def explode(input, antall=24):
    størrelse = len(input) // antall
    fragmenter = [input[i:i+størrelse] for i in range(0, len(input), størrelse)]
    return fragmenter

with open("pinneved.txt", "r") as f:
    pinneved = f.read()
    
steg_1 = explode(pinneved)

otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]

steg_2 = ["","","","","","","","","","","","","","","","","","","","","","","",""]
for i, otp_number in enumerate(reversed(otp)):
    steg_2[otp_number] = steg_1[i]

steg_3 = [''.join(chr(ord(c) - 2) for c in fragment) for fragment in steg_2]
    
print("".join(steg_3))
