def explode(input, antall=24):
    størrelse = len(input) // antall
    fragmenter = []
    
    for i in range(0, len(input), størrelse):
        fragment = input[i:i+størrelse]
        fragmenter.append(fragment)

    return fragmenter

with open("pinneved.txt", "r") as f:
    pinneved = f.read()
    
steg_1 = explode(pinneved)

otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]

steg_2 = ["","","","","","","","","","","","","","","","","","","","","","","",""]
for i, otp_number in enumerate(reversed(otp)):
    steg_2[otp_number] = steg_1[i]

steg_3 = []
for fragment in steg_2:
    new_fragment = ''
    for c in fragment:
        new_fragment += chr(ord(c) - 2)
    steg_3.append(new_fragment)
    
print("".join(steg_3))
