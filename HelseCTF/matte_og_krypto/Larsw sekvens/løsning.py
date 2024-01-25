# Lang sekvenser
long_sequence = "AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAA"

# Korte sekvenser
short_sequences = [
    "AjAA", "AiAA", "kAAl", "AAnA", "AiAA", "hAAi", "AnAA", "iAAj", "pAAq", "QAAR",
    "AAlA", "AYAA", "LAAM", "AgAA", "AgAA", "AAiA", "AiAA", "WAAX", "mAAn", "nAAo",
    "jAAk", "AZAA", "AlAA", "LAAM", "AqAA"
]

# Finn posisjonen til hver kort sekvens i den lange sekvensen
for seq in short_sequences:
    print(chr(long_sequence.find(seq)), end="")

   
