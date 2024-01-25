with open("rockyou.txt", "r", encoding="latin-1") as f:
    rockyou = f.read()

with open("mellomrom.txt", "w") as w:
    for i in rockyou.split("\n"):
        if " " in i:
            w.write(i + "\n")