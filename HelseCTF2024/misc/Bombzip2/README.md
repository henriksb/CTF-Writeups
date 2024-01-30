### Bombzip2
Vi har en bzip2-fil som inneholder et komprimert flagg, men den utpakka fila er kjempestor. Mange, mange terabyte, og flagget ligger helt på slutten. Hvis du prøver å pakke den ut fyller du sannsynligvis harddiskene dine. Derfor er oppgaven uløselig.

#### Filer
flag.bz2

#### Løsning
Flagget ligger inne i en "zip-bomb". En zip-bomb er en fil som har en liten størrelse mens innholdet er komprimert, men en enorm størrelse om det skulle blitt dekomprimert. For å hente dette flagget må vi åpne filen i en HEX editor, som HxD. Åpner vi den opp ser vi den følgende linjen gjentatt en god del ganger:
```
0028c580: a90a 8097 3141 5926 5359 0e09 e2df 015f  ....1AY&SY....._
0028c590: 8e40 00c0 0000 0820 0030 804d 4642 a025  .@..... .0.MFB.%
```
Men, hvis vi treffer bunnen ser vi noe annet:
```
00e47370: 8e40 00c0 0000 0820 0030 804d 4642 a025  .@..... .0.MFB.%
00e47380: a90a 8097 3141 5926 5359 890d 70a4 005d  ....1AY&SY..p..]
00e47390: be5b 80c0 1004 004c 0000 00bb c71e 2a00  .[.....L......*.
00e473a0: 0820 0054 36a8 9b48 d019 1820 8aa6 800d  . .T6..H... ....
00e473b0: 00d3 6a40 2aa2 8a92 92a2 a082 8116 695a  ..j@*.........iZ
00e473c0: 4bbf 2bc5 2bd4 615d f0d1 afb7 d736 6bad  K.+.+.a].....6k.
00e473d0: a7de 2309 66c9 0008 100b f177 2453 8509  ..#.f......w$S..
00e473e0: 0224 327f 80                             .$2..

```

Jeg er ikke så kjent med akkurat dette filformatet, men noe av dette kan være en sluttsignatur. Uansett så blir vi fortalt at flagget ligger helt på slutten av filen, så vi kopierer dette, i tillegg til startsignaturen av filen og setter det i sammen til en ny. Dette kan gjøres med CTRL-C og CTRL-V i HxD. Da kan man behandle filen som en vanlig bz2 fil og hente ut flagget.

`helsectf{b0mb3rm4n_s3nt_y0u_a_fl4g}`