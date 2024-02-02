n_47  = "int(repr(int(not())+int(not())+int(not())+int(not()))+repr((int(not())+int(not()))*(int(not())+int(not())+int(not()))+int(not())))"
n_108 = "int(repr(int(not()))+repr(int())+repr((int(not())+int(not())+int(not())+int(not()))*(int(not())+int(not()))))"
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
n_120 = "int(repr(int(not()))+repr(int(not())+int(not()))+repr(int()))"

path = "/lol/hemmeligmappe/flagg.txt"

script_content = ""

for i in path:
    if ord(i) == 47:
        script_content += "chr(" + n_47 + ")+"
    elif ord(i) == 108:
        script_content += "chr(" + n_108 + ")+"
    elif ord(i) == 111:
        script_content += "chr(" + n_111 + ")+"
    elif ord(i) == 104:
        script_content += "chr(" + n_104 + ")+"
    elif ord(i) == 101:
        script_content += "chr(" + n_101 + ")+"
    elif ord(i) == 109:
        script_content += "chr(" + n_109 + ")+"
    elif ord(i) == 105:
        script_content += "chr(" + n_105 + ")+"
    elif ord(i) == 103:
        script_content += "chr(" + n_103 + ")+"
    elif ord(i) == 112:
        script_content += "chr(" + n_112 + ")+"
    elif ord(i) == 102:
        script_content += "chr(" + n_102 + ")+"
    elif ord(i) == 97:
        script_content += "chr(" + n_97 + ")+"
    elif ord(i) == 46:
        script_content += "chr(" + n_46 + ")+"
    elif ord(i) == 116:
        script_content += "chr(" + n_116 + ")+"
    elif ord(i) == 120:
        script_content += "chr(" + n_120 + ")+"

script_content = script_content.rstrip("+") + "))"

with open("solve.py", "w") as file:
    file.write("print(*open(")
    file.write(script_content)
