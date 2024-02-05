### Short not cipher
Denne oppgaven er helt lik not cipher, bare at programmet du sender inn må være kortere enn 5000 tegn.

#### Løsning
Denne oppgaven er en variant av "not cipher", med en tilleggsutfordring: løsningen må være under 5000 tegn. For å oppnå dette må vi finne en mer kompakt metode for å konvertere tall til bokstaver. I den opprinnelige "not cipher"-oppgaven benyttet jeg kun addisjon, men vi kan også utnytte multiplikasjon og potensregning. For å knekke denne koden eksperimenterte jeg med forskjellige kombinasjoner av multiplikasjon og potensregning på ulike tall for å minimere lengden på uttrykket. Følgende beregninger ble brukt for å nå frem til en mer kondensert løsning:

```python
n_47  = "(int(not())+int(not())+int(not()))**(int(not())+int(not())+int(not()))+(int(not())+int(not())+int(not())+int(not())+int(not()))*(int(not())+int(not())+int(not())+int(not()))"
n_108 = "(int(not())+int(not())+int(not()))**(int(not())+int(not()))*(int(not())+int(not())+int(not())+int(not()))*(int(not())+int(not())+int(not()))"
n_111 = "(int(not())+int(not())+int(not()))**(int(not())+int(not())+int(not())+int(not()))+(int(not())+int(not())+int(not()))**(int(not())+int(not())+int(not()))+(int(not())+int(not())+int(not()))"
n_104 = "(int(not())+int(not())+int(not())+int(not())+int(not()))**(int(not())+int(not()))*((int(not())+int(not())+int(not())+int(not())))+(int(not())+int(not())+int(not())+int(not()))"
n_101 = "(int(not())+int(not())+int(not())+int(not())+int(not()))**(int(not())+int(not()))*((int(not())+int(not())+int(not())+int(not())))+(int(not()))"
n_109 = "(int(not())+int(not())+int(not())+int(not())+int(not()))**(int(not())+int(not()))*((int(not())+int(not())+int(not())+int(not())))+(int(not())+int(not())+int(not()))*(int(not())+int(not())+int(not()))"
n_105 = "(int(not())+int(not())+int(not())+int(not())+int(not()))**(int(not())+int(not()))*((int(not())+int(not())+int(not())+int(not())))+(int(not())+int(not())+int(not())+int(not())+int(not()))"
n_103 = "(int(not())+int(not())+int(not())+int(not())+int(not()))**(int(not())+int(not()))*((int(not())+int(not())+int(not())+int(not())))+(int(not())+int(not())+int(not()))"
n_112 = "(int(not())+int(not())+int(not()))**(int(not())+int(not())+int(not())+int(not()))+(int(not())+int(not())+int(not()))**(int(not())+int(not())+int(not()))+(int(not())+int(not())+int(not()))+int(not())"
n_102 = "(int(not())+int(not())+int(not())+int(not())+int(not()))**(int(not())+int(not()))*((int(not())+int(not())+int(not())+int(not())))+(int(not())+int(not()))"
n_97  = "(int(not())+int(not())+int(not()))**(int(not())+int(not())+int(not())+int(not()))+(int(not())+int(not()))**(int(not())+int(not())+int(not())+int(not()))"
n_46  = "(int(not())+int(not())+int(not())+int(not())+int(not()))*(int(not())+int(not())+int(not())+int(not())+int(not())+int(not())+int(not())+int(not())+int(not()))+int(not())"
n_116 = "(int(not())+int(not())+int(not())+int(not())+int(not()))**(int(not())+int(not()))*((int(not())+int(not())+int(not())+int(not())))+(int(not())+int(not()))**(int(not())+int(not())+int(not())+int(not()))"
n_120 = "(int(not())+int(not()))*(int(not())+int(not())+int(not()))*(int(not())+int(not())+int(not())+int(not())+int(not()))*(int(not())+int(not())+int(not())+int(not()))"

path = "/lol/hemmeligmappe/flagg.txt"
```

Det fullstendige skriptet ligger [her](https://github.com/henriksb/CTF-Writeups/blob/main/HelseCTF2024/misc/Short%20not%20cipher/solve_generator_short.py).

Igjen må vi også bruke et [bash skript](https://github.com/henriksb/CTF-Writeups/blob/main/HelseCTF2024/misc/Short%20not%20cipher/send.sh) for å sende denne mengden data.

`helsectf{h4rd3r_b3tt3r_f4s73r_sh0rt3r}`

#### Bedre løsning
Det er en liten konkurranse om hvem som klarer å få den kortest mulig. Jeg hadde helt glemt `repr` funksjonen, som gjør tall on til string. Ved bruk av denne kan vi for eksempel gjøre `1+1=11`. En bedre løsning er:

```python
n_47  = "(int(not())+int(not())+int(not()))**(int(not())+int(not())+int(not()))+int(repr(int(not())+int(not()))+repr(int()))"
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
n_116 = "int(repr(int(not()))+repr((int(not())+int(not()))**(int(not())+int(not())+int(not())+int(not()))))"
n_120 = "int(repr(int(not()))+repr(int(not())+int(not()))+repr(int()))"
```
Jeg har også gjort om dobbeltkonsonanter til bokstav*2, istedenfor å gjøre bokstav+bokstav. Dette reduserer lengden bittelitt.

```python
# Bytt dobbeltkonsonanter med *2, istedenfor å plusse de på hverandre
script_content = script_content.replace(("chr(" + n_109 + ")+") * 2, "chr(" + n_109 + double) # m
script_content = script_content.replace(("chr(" + n_112 + ")+") * 2, "chr(" + n_112 + double) # p
script_content = script_content.replace(("chr(" + n_103 + ")+") * 2, "chr(" + n_103 + double) # p
```
Det er mulig man også kan bruke `oct` eller lage HEX tall som er kortere.

Størrelse på resultat: 2495 bytes

Det viser seg at man bare trengte å bruke "flagg.txt", da vi var i samme mappe som flagget. Burde kanskje ha prøvd det, da filbanen er absolutt, ikke relativ.
