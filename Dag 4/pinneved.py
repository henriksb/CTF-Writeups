"""TEMMELIG HEMMELIG"""
"""Sør-Polar Sikkerhetstjeneste"""
"""Høyeksplosivt script for tilintetgjørelse av Julenissens slede"""


otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]

def explode(input, antall):
    størrelse = len(input) // antall
    print("Størrelse: " + str(størrelse))
    fragmenter = []
    
    for i in range(0, len(input), størrelse):
        fragment = input[i:i+størrelse]
        fragmenter.append(fragment)
    
    return fragmenter

with open("slede.txt", "r") as file:
    slede = file.read()

print(slede)

bang = explode(slede, 24)
print("1: ", end="")
print(bang)

eksplosjon = []
for fragment in bang:
    new_fragment = ''
    for c in fragment:
        new_fragment += chr(ord(c) + 2)
    eksplosjon.append(new_fragment)

print("2: ", end="")
print(eksplosjon)

pinneved = []
for i in reversed(otp):
    pinneved.append(str(eksplosjon[i]))

print("3: ", end="")
print(pinneved)

with open("test.txt", "w") as file:
    file.write(''.join(pinneved))


