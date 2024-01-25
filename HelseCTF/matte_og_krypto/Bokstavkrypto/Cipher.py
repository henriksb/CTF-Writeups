with open("chiffertekst.txt", "r") as cipher:
    cipher = cipher.read()

with open("klartekst.txt", "r") as cleartext:
    cleartext = cleartext.read()

l = []

for i in range(0,len(cleartext)):
    l.append(ord(cipher[i])-ord(cleartext[i]))
    print(ord(cipher[i])-ord(cleartext[i]), cipher[i], cleartext[i])

#print(l)