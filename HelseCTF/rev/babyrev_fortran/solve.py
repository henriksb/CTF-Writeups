flagg = "gemredsf|k3oFe`r1E2n`e02j_qqoh`MNdR8d_j^Fpqts`n`80~"

svar = ""

for i, char in enumerate(flagg):
    offset = (1, 0, -1)[i % 3]
    svar += chr(ord(char) + offset)

print(svar)
    