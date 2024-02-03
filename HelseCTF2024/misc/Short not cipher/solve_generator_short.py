n_47  = "((int(not())+int(not()))*(int(not())+int(not())+int(not())))**(int(not())+int(not()))+int(repr(int(not()))+repr(int(not())))"
n_108 = "int(repr(int(not()))+repr(int())+repr((int(not())+int(not()))**(int(not())+int(not())+int(not()))))"
n_111 = "int(repr(int(not()))+repr(int(not()))+repr(int(not())))"
n_104 = "int(repr(int(not()))+repr(int())+repr(int(not())+int(not())+int(not())+int(not())))"
n_101 = "int(repr(int(not()))+repr(int())+repr(int(not())))"
n_109 = "int(repr(int(not()))+repr(int())+repr((int(not())+int(not())+int(not()))**(int(not())+int(not()))))"
n_105 = "int(repr(int(not()))+repr(int())+repr(int(not())+int(not())+int(not())+int(not())+int(not())))"
n_103 = "int(repr(int(not()))+repr(int())+repr(int(not())+int(not())+int(not())))"
n_112 = "int(repr(int(not()))+repr(int(not()))+repr(int(not())+int(not())))"
n_102 = "int(repr(int(not()))+repr(int())+repr(int(not())+int(not())))"
n_97  = "int(repr((int(not())+int(not())+int(not()))**(int(not())+int(not())))+repr((int(not())+int(not()))*(int(not())+int(not())+int(not()))+int(not())))"
n_46  = "int(repr(int(not())+int(not())+int(not())+int(not()))+repr((int(not())+int(not()))*(int(not())+int(not())+int(not()))))"
n_116 = "int(repr(int(not()))+repr(int(not()))+repr((int(not())+int(not()))*(int(not())+int(not())+int(not()))))"
n_120 = "int(repr(int(not()))+repr(int(not())+int(not()))+repr(int()))" # x
# 0x = repr(int())+chr(int(repr(int(not()))+repr(int(not())+int(not()))+repr(int())))

n_values = {
    47: n_47,
    108: n_108,
    111: n_111,
    104: n_104,
    101: n_101,
    109: n_109,
    105: n_105,
    103: n_103,
    112: n_112,
    102: n_102,
    97: n_97,
    46: n_46,
    116: n_116,
    120: n_120,
}

path = "/lol/hemmeligmappe/flagg.txt"

def chr_from_n(n):
    return f"chr({n})"


# Legg til ascii verdien av hver bokstav i "path" med "n_xxx"-listen
script_content = "+".join(chr_from_n(n_values[ord(i)]) for i in path if ord(i) in n_values) + "+"

# Fiks parentes og feilplasserte plusstegn
script_content = script_content.rstrip("+") + "))"

# Bytt dobbelkonsonanter med *2, istedenfor å plusse de på hverandre
for i in [n_109, n_112, n_103]:
    script_content = script_content.replace(("chr(" + i + ")+") * 2, "chr(" + i + ")*(int(not())+int(not()))+")


with open("solve.py", "w") as file:
    file.write("print(*open(")
    file.write(script_content)
