### Rocky Balboa
Etter grundige undersøkelser på internett, har vårt sikkerhetsteam oppdaget en mistenkelig video. Videoen viser en hacker som bryter seg inn i et høyt sikret datasystem. Vi har også oppdaget et passordhash som ser ut til å være relatert til hackeren: $2b$14$WpeU3BB4A1FpeOoTRa100O3/a5RSzhnvFJyxOEZ3v2z4It/gM71Eu

Det virker som hackeren liker å høre på Rocke Deg sanger mens hen sorterer igjennom samlingen sin av forskjellige ordbøker. Ordbøker er veldig viktig når man skal knekke passord!

Oppgaven går ut på å knekke passordet fra hashen over. Passordet leveres wrappet i flaggformatet, slik: helsectf{<passsord>}

PS: passordet innholder opptil flere mellomrom

#### Løsning

Denne oppgaveteksten inneholder flere ledetråder. Begrepet "rock" blir gjentatt i både tittelen og beskrivelsen. Gitt konteksten om passordknekking, virker det å peke tydelig mot `rockyou.txt`, en av de største og beste passordlistene.

Det andre hintet er `PS: passordet inneholder opptil flere mellomrom`.

Det siste vi må finne ut er hvilken hash dette er. For å finne ut av det kan man bruke en [hash identifier](https://hashes.com/en/tools/hash_identifier). Her virker det som om "blowfish" er brukt.

Da er det bare å sette i sammen en hashcat kommando til å knekke passordet: `hashcat -m 3200 -a 0 password.txt rockyou.txt -o out`. Problemet her er at blowfish kan være en veldig tung hash å knekke. Her må vi bruke det andre hintet i oppgaven, som sier at passordet inneholder opptil flere mellomrom. Da kan vi generere en ny versjon av rockyou, hvor vi fjerner alt som ikke inneholder mellomrom. Dette ble gjort med følgende script:

```python
with open("rockyou.txt", "r", encoding="latin-1") as f:
    rockyou = f.read()

with open("mellomrom.txt", "w") as w:
    for i in rockyou.split("\n"):
        if " " in i:
            w.write(i + "\n")
```
Da er det bare å kjøre hashcat på nytt med den nye tekstfilen: `hashcat -m 3200 -a 0 password.txt mellomrom.txt -o out`.

`helsectf{being so stupid becuz of cheer}`