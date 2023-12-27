with open("random_text.bin", "r") as f:
    f = f.read()

segment = sorted(f.split("\u0000"), key=len)

flagg = ""
for bokstav in segment[1:]:
    flagg+=bokstav[0]

    if bokstav[0] == "}":
        break

print(flagg)