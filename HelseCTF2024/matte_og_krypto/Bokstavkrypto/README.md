# Bokstavkrypto

Analyseavdelingen har fanget opp en klartekst med tilhørende chiffertekst, men det siste avsnittet av klarteksten mangler.

Alle de uavhengige kryptografene våre insisterer på at det er viginere-cipher som er brukt, og vi stoler på dem, men vi kan ikke skjønne hvordan de kan ha rett.

Analyseavdelingen mangler kapasitet til å se på dette, og håper du har tid. De foreslår at du analyserer de første avsnittene, så skal du greie å dekryptere den siste delen.



#### Hint
Analyseavdelingen er sikre på at kryptoen er 100% Vigenèrechiffer. En kryptolog er satt på saken. Hen har begynt å analysere bokstavene med piler og baner.

Se vedlagt bilde (til oppgaven)

![hint](bokstavkrypto_piler_og_baner.png)

#### Filer
chiffertekst.txt

klartekst.txt

bokstavkrypto_piler_og_baner.png


## Løsning
Etter fire dager med kun én person som hadde løst opppgaven, kom de ut med et hint. Dette hintet viser tre grupper med bokstaver, hvor pilene viser hvilke klartekst bokstaver som går til hvilke chiffertekst bokstaver. Etter å ha kikket litt på dette bildet innså jeg at det var akkurat den samme koblingen jeg hadde funnet selv ved å hente bokstavende på samme indeks.

Listen med bokstavkoblinger jeg genererte er den følgende:
```python
{'ø': ['d', 's'], 'q': ['e', 'o', 'i', 'r', 'p'], 'w': ['t', 'r', 'o', 'p'], 'x': ['v', 'n', 'm'], 'l': ['a', 'g', 's'], 'i': ['r', 't', 'y', 'p'], 't': ['e', 'i', 'u', 'q'], 'f': ['g', 'k'], 'g': ['a', 'l', 'h', 'k'], 'z': ['n', 'b', 'c'], 'u': ['e', 'o', 't', 'r', 'p'], 'v': ['n', 'x'], 'æ': ['f', 'd', 'a', 'j'], 'y': ['r', 'e', 'o', 'i'], 'a': ['s', 'k', 'g', 'f'], 'd': ['h', 'ø', 'f'], 'p': ['i', 'u'], 'h': ['l', 's', 'j'], 'å': ['e', 'i', 'o', 'u'], 'k': ['a', 'f', 'l', 'æ'], 's': ['d', 'l', 'g'], 'o': ['t', 'u', 'å'], 'c': ['m', 'b'], 'n': ['v', 'c'], 'j': ['d'], 'e': ['t', 'p', 'q'], 'm': ['b', 'v'], 'b': ['m', 'c'], 'r': ['u']}
```
Jeg genererte et bilde av mine koblinger for å se om det var noe likhet:

![selvgenerert](piler_og_baner.png)

Plasseringen på ting er ikke det samme, men innholdet er identisk (med unntak av pilretningen, men det er ikke relevant).

Jeg tenkte at man kanskje kunne gjette seg frem til hva flagget kunne være med bruk av disse koblingene. Jeg prøvde å generere alle mulige kombinasjoner av flagget i tillegg til å sammenligne med norske, franske og latinske ordbøker. Ingen lykke her. Så jeg prøvde å finne ord som var >80% like, ingen lykke der heller. Jeg prøvde til og med å bruke ulike frekvensanalyser og sannsynlighetsberegning for å finne det mest sannsynlige flagget, som ga meg følgende resultater:

`frekvensanalyse (bokstaver) + gyldige bokstaver = hellicyd{didehruidee-kdcchirddrkbblhh}`

`frekvensanalyse (nøkkel)    + gyldige bokstaver = aelsemra{aedlaetedee-sannareddesbmlaa}`

Det er jo noen bokstaver der som er korrekte, men ikke nok til at jeg kan gjette flagget. Det eneste jeg fant ut med disse metodene var at det siste avsnittet var latinsk, og etter å ha funnet svaret fikk jeg bekreftet at jeg med suksess hadde klart å bruteforce store deler av det siste avsnittet. Dessverre hjelper ikke dette mye med flagget.

Siden det ikke var noen mønster i nøkkelen jeg genererte for klarteksten, og ingenting i frekvensanalysen eller sannsynlighetsberegningen måtte det være en annen løsning.

Kikker man på bildet kan man se at de tre gruppene det er delt inn i er rader på tastaturet:

`qwertyuiopå`

`asdfghjkløæ`

`zxcvbnm`

Hver bokstav blir kryptert til en annen bokstav på samme rad. Dette kan bety at teksten kan ha vært kryptert i tre omganger, en gang for hver rad av tastaturet. Hvis vi prøver å manuelt finne nøkkelen til hver bokstavgruppe får vi følgende resultat:

Alfabet: qwertyuiopå \
Nøkkel: poteter

Alfabet: asdfghjkløæ \
Nøkkel: klægg

Alfabet: zxcvbnm \
Nøkkel: nvc

Får å finne nøkkelen prøver vi oss frem til vi får forventet resultat, det vil si at bokstavene som er i alfabetet vårt endrer seg til det vi har i klarteksten. Etter vi har fullført et alfabet, kopierer vi resultatet fra det og bruker det som chiffertekst på neste alfabet. Vi gjør dette for alle alfabetene Dette gir oss flagget:

`helsectf{duklartedet-facbaeeddefbbdaa}`

Her er en forklaring med eksempler fra Python. Funksjonen `dekrypter` tar tre argumenter:

1. `chiffertekst`: Teksten som skal dekrypteres.
2. `nøkkel`: Ordet eller setningen som brukes til å dekryptere teksten.
3. `alfabet`: En string eller liste som representerer alfabetet brukt i chifferet.

```python
def dekrypter(chiffertekst, nøkkel, alfabet):
    """Dekrypter Vigenere chiffer"""
    nøkkel_index = 0
    dekryptert_tekst = ""
    
    for char in chiffertekst:
        if char in alfabet:
            # Finn posisjonen til bokstaven i alfabetet og nøkkelbokstaven
            char_index = alfabet.index(char)
            nøkkel_char_index = alfabet.index(nøkkel[nøkkel_index % len(nøkkel)])
            # Beregn ny posisjon etter å ha trukket fra nøkkelposisjonen (med mod for å sikre at vi holder oss innenfor alfabetet)
            ny_pos = (char_index - nøkkel_char_index) % len(alfabet)
            dekryptert_tekst += alfabet[ny_pos]
            nøkkel_index += 1
        else:
            dekryptert_tekst += char  # Kopierer alt som ikke finnes i alfabetet
    
    return dekryptert_tekst
```
Innenfor funksjonen itereres det over hver bokstav i chifferteksten. Hvis bokstaven er en del av det gitte alfabet, beregnes dens opprinnelige posisjon ved hjelp av nøkkelbokstavens posisjon. Hvis tegnet ikke er en del av alfabet, blir det lagt til i dekryptert_tekst uten endringer. Dette er viktig, slik at vi ikke endrer på bokstaver som ikke er i alfabetet.

 Hvis vi tar den første linjen fra begge tekstfilene våre har vi:

`øqw xli tx fgzl uv æylxaaxgvx` fra chifferteksten, og\
`det var en gang en franskmann` fra klarteksten.

I første omgang prøver vi å dekryptere bokstavene fra tastaturets topprad: `qwertyuiopå`.
```python
dekryptering_del_1 = dekrypter(chiffertekst, "poteter", "qwertyuiopå")
```
Da gjør gjør vi den følgende endringen:

`øqw xli tx fgzl uv æylxaaxgvx` =\
`øet xlr ex fgzl ev ærlxaaxgvx`

Vi kan her se at bokstavene fra `qwertyuiopå` er byttet ut til bokstavene vi har i klarteksten. Gjør vi dette for alle alfabetene får vi:

```python
alfabet = ["qwertyuiopå", "asdfghjkløæ", "zxcvbnm"]

dekryptering_del_1 = dekrypter(chiffertekst,       "poteter", alfabet[0])
>> øet xlr ex fgzl ev ærlxaaxgvx

dekryptering_del_2 = dekrypter(dekryptering_del_1, "klægg",   alfabet[1])
>> det xar ex gazg ev fraxskxavx

dekryptering_del_3 = dekrypter(dekryptering_del_2, "nvc",     alfabet[2])
>> det var en gang en franskmann
```

Å gjette seg frem til nøkkelen er ikke altfor vanskelig, da første bokstav i nøkkelen kun endrer første bokstav i chifferteksten. Vi trenger derfor ikke å finne hele nøkkelen for at resultatet skal gi mening. I tillegg til dette så er hver nøkkel en kombinasjon av bokstaver som er på samme rekke av tastaturet.

Et viktig aspekt ved Vigenere-chifferet er nøkkelgjentakelse. Hvis nøkkelen er kortere enn teksten, gjentas nøkkelen til den matcher lengden på teksten. I funksjonen håndteres dette ved å bruke modulusoperatoren for å sirkulere gjennom nøkkelens bokstaver.
