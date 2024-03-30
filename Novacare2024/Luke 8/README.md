# Brainfuck 101
Brainfuck er et minimalistisk programmeringsspråk, med kun åtte kommandoer – hver kommando skrives med kun ett tegn.

Dagens oppgave går ut på å skrive kode i en ekstra minimalistisk variant av språket brainfuck. Dagens kodeord er koden som skriver ut det første tegnet i ditt eget brukernavn. Og hvis brukernavnet ditt inneholder spesialtegn som ikke enkelt lar seg skrive ut i brainfuck, kan du isteden svare med minimalistisk brainfuck kode som skriver ut «yo», altså et ord på to små bokstaver.

I dagens variant av brainfuck må du forholde deg til:

Kun følgende kommandoer er tillatt
```
>
<
+
-
.
```
Ingen loops \
Ingen input \
Du er begrenset til 10 celler \
Det var det! Enkelt og greit!

Lykke til!

## Løsning

Tid brukt: 5 minutter

Jeg misforstod oppgaven litt (prøvde å gjøre den raskt og leste ikke oppgaveteksten) og trodde ordet vi skulle skrive var "yo". Etter å ha lest teksten skikkelig innså jeg at det var første bokstaven av brukernavnet vårt vi skulle skrive, uten loops og input.

For å gjøre dette i brainfuck bruker man ASCII verdien til bokstaven og skriver samme antall med "+".

`python3 -c "print('+'*ord('H')+'.')"`

Kodeord: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
