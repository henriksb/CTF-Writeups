with open("Oppskrift.txt", 'r', encoding='utf-8') as file:
    innhold = file.read()

for bokstav in range(len(innhold)):
    if innhold[bokstav] == '\u200d':
        print(innhold[bokstav+1], end="")