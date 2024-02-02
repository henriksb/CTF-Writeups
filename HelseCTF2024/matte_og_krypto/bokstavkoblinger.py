import sys

with open("chiffertekst.txt", "r") as cipher_file:
    cipher = [x for x in cipher_file.read() if x.isalpha()]

with open("klartekst.txt", "r") as cleartext_file:
    cleartext = [x for x in cleartext_file.read() if x.isalpha()]

cipher_to_cleartext = {}
cleartext_to_cipher = {}

for i in range(len(cleartext)):
    if cipher[i] not in cipher_to_cleartext:
        cipher_to_cleartext[cipher[i]] = []

    if cleartext[i] not in cipher_to_cleartext[cipher[i]]:
        cipher_to_cleartext[cipher[i]].append(cleartext[i])

    if cleartext[i] not in cleartext_to_cipher:
        cleartext_to_cipher[cleartext[i]] = []

    if cipher[i] not in cleartext_to_cipher[cleartext[i]]:
        cleartext_to_cipher[cleartext[i]].append(cipher[i])

argv = sys.argv[1]
try:
    print("Ciphr ({0}) --> Clear ({1})".format(argv, cipher_to_cleartext[argv]))
    print("Clear ({0}) --> Ciphr ({1})".format(argv, cleartext_to_cipher[argv]))
except KeyError:
    print(None)






