### Zellweger
Jeg brukte DALL-E til å generere et bilde med følgende beskrivelse:

`ones and zeros as electrical pulses over a set of power lines`

Jeg syntes det var en passende beskrivelse siden jeg har skjult et tier-bit enkodet flagg i bildet.

Husk! Det er viktig å ha en god start puls i hvert ledd av den minst betydninsgfulle biten i diagrammet.

#### Filer
zellweger.png

#### Løsning
Oppgaveteksten har mange gode hint som hjelper oss med å løse denne oppgaven. Vi leter etter et tier-bit (10-bit) enkodet flagg, og det finner man ved å se på LSB (least significant bit) verdien.

LSB, eller least significant bit, er tallet som er helt til høyre i et binærtall. LSB verdien i `00000001` er `1`. For å finne flagget må vi hente ut alle disse verdiene fra bildet. Gjør vi det får vi en enormt stor tekstfil med binærtall. På toppen av tekstfilen finner vi massevis av enere, helt til det plutselig stopper, og helt på bunnen finner vi også noen enere.

Måten jeg hentet LSB verdiene på var med følgende script:
```python
def extract_lsb(pixel):
    # piksel er en tupple med (R, G, B), vi må få LSB fra hver del
    return (pixel[0] & 1, pixel[1] & 1, pixel[2] & 1)


img_path = 'zellweger.png'
img = Image.open(img_path)

img_data = np.array(img)

# Ekstraher LSB fra hele bildet
lsb_data = np.apply_along_axis(extract_lsb, 2, img_data)

# Siden bildet kan være stort, og vi ønsker og returnere en tekstbasert representasjon,
# må vi flate ut lsb_data og konvertere den til en streng med 0-er og 1-ere.
# Så setter vi sammen LSB-ene for R,G,B for hver piksel.
lsb_flat = lsb_data.flatten()
lsb_str = ''.join(map(str, lsb_flat))

# Korter ned på den enorme mengden data
binary = lsb_str[0:27000]

print(extract_following_bits(binary))
```

Konverterer man binærtallenepå slutten til tekst får man denne linken: https://de.wikipedia.org/wiki/Decabit. Denne konversjonen er binær til ascii.

Prøver man å gjøre det samme for binærtallene på toppen får man bare tull. Disse tallene må man konvertere med en [Decabit decoder](https://www.dcode.fr/decabit-code).


`helsectf{bilde_steg0_done_r1ght__no_pun_intend3d_:):)}`

