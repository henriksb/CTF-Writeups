# Larsw sekvens

Vi har fanget opp en spesiell sekvens AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAA med en liste av korte tegn:

```
AjAA
AiAA
kAAl
AAnA
AiAA
hAAi
AnAA
iAAj
pAAq
QAAR
AAlA
AYAA
LAAM
AgAA
AgAA
AAiA
AiAA
WAAX
mAAn
nAAo
jAAk
AZAA
AlAA
LAAM
AqAA
```

Kameraten til Lars sier at han kan ha brukt dette til å kryptere flagget. Lars har muligens en overdreven interesse i sekvenser laget av Nicolaas Govert.


## Løsning
Nicolaas Govert de Bruijn er skaperen av de Bruijn sekvensen. En de Bruijn-sekvens kan forklares på en enkel måte ved å tenke på en spesiell type puslespill. Forestill deg at du har et alfabet (for eksempel bokstavene A og B, eller tallene 0 og 1) og du ønsker å sette sammen en så kort rekkefølge som mulig hvor du kan finne hver tenkelig kombinasjon av bokstaver eller tall av en bestemt lengde nøyaktig én gang.

For eksempel, hvis du bare bruker tallene 0 og 1 og ønsker at hver mulige kombinasjon av to tall skal vises, kan en de Bruijn-sekvens være 00110. I denne sekvensen finner du 00, 01, 11, og 10. Hvis du ser på det som en ring eller en sirkel, ser du at etter 0 kommer en annen 0 (00), etterfulgt av en 1 (01), og så videre. På denne måten har du alle par av tallene uten å gjenta deg selv mer enn nødvendig.

Så, en de Bruijn-sekvens er en smart måte å organisere en rekke med symboler på slik at hver mulig kort sekvens av en gitt lengde er inkludert nøyaktig én gang, og dette gjøres på den kortest mulige måten. Det er som å ha en superkompakt nøkkelring med alle mulige nøkler (kombinasjoner), der hver nøkkel er unik og lett å finne.

For å finne flagget, finner vi indeksen til hver av de korte frekvensene i den lange sekvensen. Deretter gjør vi dette om til en bokstav.


```python
lang_sekvens = "AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAA"

korte_sekvenser = [
    "AjAA", "AiAA", "kAAl", "AAnA", "AiAA", "hAAi", "AnAA", "iAAj", "pAAq", "QAAR",
    "AAlA", "AYAA", "LAAM", "AgAA", "AgAA", "AAiA", "AiAA", "WAAX", "mAAn", "nAAo",
    "jAAk", "AZAA", "AlAA", "LAAM", "AqAA"
]

# Finn posisjonen til hver kort sekvens i den lange sekvensen
for sek in korte_sekvenser:
    print(chr(lang_sekvens.find(sek)), end="")

>> helsectf{0mG!__deBruiJn!}
```
