### debug_rat

En god RAT går aldri av moten! Vi har deployet en test, men glemte å slå av feilsøkingsgrensesnittet og andre skjulte kommandoer.

Kan du ta kontrollen på råtta og se om det er mulig å få ut flagget som ligger lagret på /flag.txt?

Oppdatering: Obs! Noen kan finne flagget på en måte som inneholder en feil - det har doble underscores '__'. Korrekt flagg er uten doble underscores.

PS! Binarien er en fult fungerende Remote Access Trojan som gir Remote Code Execution. I god stil er derfor oppgavefilen pakket i en kryptert zip. (passord: infected)


#### Filer
debug_rat.zip

#### Løsning
Denne oppgaven løses uten en debugger. Deler av flagget kan man bare få ved å koble til serveren, men man får ELF-filen for å analysere innholdet. Programmet jeg brukte er Ghidra. Her er hvordan jeg fikk de tre delene av flagget:

1. Kjør `strings` kommandoen og se igjennom resultatet. Her kan man finne `Orifice???}`.  Dette ser ut som slutten på et flagg.

2. Dekompilerer man filen og går inn i funksjonen `FUN_00101ef2` ser man: 
    ```c
    if (((local_588 == 6)
    ```
    Denne if-setningen sjekker om lengden på input er 6. Skriver vi en input med lengde 6 i programmet, som for eksempel `AAAAAA`, får vi del 2 av flagget: `_Netbus_aNd_Back`.

3. Del tre av flagget kan man bare få av å koble til den eksterne serveren, men vi kan finne ut hvordan man henter det ved å analysere koden. I den samme funksjonen kan vi finne:
    ```c
    if ((((local_588 == 8) && (local_4c8[3] == ' ')) && (local_4c4 == '1')) &&
    (((local_4c3 == '3' && (local_4c2 == '3')) && (cStack_4c1 == '7')))) {
    local_584 = 3;
    }
    ```
    Her kan man se at den sjekker om lengden på input er 8, og at man har skrevet 1337. Denne if-setningen ligger inne i "cat" if-setningen. Dette betyr at kommandoen den leter etter er "CAT 1337", som har en lengde på 8 tegn (mellomrom inkludert) og inneholder "1337". Skriver man "CAT 1337" inn i serveren får man del tre av flagget:

```
    > CAT 1337
     /\___/\
    /       \
   l  u   u  l
 --l----*----l--
    \   w   /     - Meow!
     ======
    /       \ __    
    l        l\ \   
    l        l/ /   flag part1 is:
    l  l l   l /    helsectf{r3meMber_
    \ ml lm /_/
```
Legger man disse tre delene i sammen får man flagget `helsectf{r3meMber_Netbus_aNd_BackOrifice???}`

#### Andre kommandoer og deler jeg ikke utforsket
I C-filen kan man også finne andre kommandoer som:

DEBUG \
HINT \
HELP

Hvis man skriver `DEBUG` finner man en if-setning inne i den. Denne setningen sjekker om lengden er 0x26, som er 38. Hvis man da skriver `DEBUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG` kjører den "Secret overwrite" og printer det ut.
```c
if (local_588 == 0x26):
```
		
Hvis man skriver `CAT` og `DAT_00105270 == null`, kjører den `_INIT_3();`. Denne delen gikk til en annen funksjon som kjørte kommandoen `cat cat_ascii.txt`.
```c
if (((local_4c8[0] == 'C') && (local_4c8[1] == 'A')) && (local_4c8[2] == 'T')) {
	if (DAT_00105280 == '\0') {
  		_INIT_3();
```
Jeg fikk heller aldri gjort som oppgaven sa, at målet var å kjøre `EXEC cat /flagg.txt`.

