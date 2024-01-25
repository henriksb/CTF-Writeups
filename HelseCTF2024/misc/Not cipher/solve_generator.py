path = "/lol/hemmeligmappe/flagg.txt"
one = "int(not())+"

script_content = "print("
#script_content = "print(*open("

for char in path:
    ascii_value = ord(char)
    char_expression = one * ascii_value
    script_content += "chr(" + char_expression[:-1] + ")+"

script_content = script_content.rstrip('+') + ")" #"))"

with open("solve.py", "w") as file:
    file.write(script_content)
