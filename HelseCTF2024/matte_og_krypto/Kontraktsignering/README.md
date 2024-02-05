### Kontraktsignering
Signaturtjenesten 2OpphøydIe signerer alle dine meldinger, bortsett fra den superviktige kontrakten.

Alle som har riktig signatur på kontrakten får flagget!

#### Filer
source.py

#### Løsning

I denne oppgaven får man kildekoden som kjører på en ekstern server:

```python
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
from flag import flag

contract = b"Dette er en superviktig kontrakt for veeldig viktige ting med store ord og uforstaaelige kruseduller."

# Standard RSA nøkkelgenerering
p = getPrime(1024)
q = getPrime(1024)
N = p*q
e = 0x10001
d = inverse(e, (p-1)*(q-1))

# Standard RSA signering/verifikasjon: https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Signing_messages
def sign(m):    
    return pow(m, d, N)

def verify(m,s):
    s = bytes_to_long(s)
    m = bytes_to_long(m)
    return sign(m) == s

print("Signaturtjenesten 2OpphøydIe signerer alle dine meldinger, bortsett fra den superviktige kontrakten:\n")
print(contract.decode())
print(f"\nN={N}")
while True:
    try:
        command = input("> ")
        if command == "sign":
            m = bytes.fromhex(input("message="))        
            if m == contract:
                quit("haha, du tru kanskje at æ e så lettlurt?? ånei du, du får itj signert den meldinga der nei!")

            print("derre va itj kontrakten, så da ska du få en signatur:")
            print("sign=", long_to_bytes(sign(bytes_to_long(m))).hex())
        elif command == "verify":
            s = bytes.fromhex(input("signature="))
            if verify(contract,s): 
                print("ja, herre e riktig signatur ja, no va du flink!")
                print("flag=", flag)
                exit(0)
            print("haha, derre va feil ja! du må hjem å øv dæ!")
        else:
            print("du kan bare bruke 'sign' eller 'verify'")
    except Exception as e:
        quit("error")
```

Oppgaven her er å forstå hva koden gjør og hvor feilen ligger. Målet er å verifisere signaturen for å få flagget, som er lagret eksternt.

RSA og Homomorfisme: RSA-kryptografi har en viktig egenskap som sier at produktet av to signaturer (under modulo N) er lik signaturen av produktet av de to opprinnelige meldingene. Dette betyr at hvis du har signaturer for to meldinger, kan du kombinere dem for å lage en signatur for meldingen som er deres produkt.

For å gjøre dette følger vi de følgende stegene:

1. Velge m1 og Beregne m2: Vi valgte en vilkårlig melding m1 og beregnet en annen melding m2 slik at m1 * m2 ≡ kontrakt (mod N). Dette ble gjort ved å velge et tilfeldig tall for m1 og deretter beregne m2 som kontrakt * invers(m1, N) mod N.

2. Få Signaturer fra Tjenesten: Siden skriptet ikke tillot signering av "kontrakt" direkte, brukte vi tjenesten til å signere både m1 og m2 separat.

3. Kombinere Signaturer: Etter å ha fått signaturer for m1 og m2, kombinerte vi disse for å lage en gyldig signatur for "kontrakt". Dette ble gjort ved å multiplisere de to signaturerne og ta resultatet modulo N.

4. Verifisere Kontrakten: Til slutt brukte vi den kombinerte signaturen for å verifisere "kontrakt" i tjenesten, som da ga oss tilgang til "flagg"-verdien.

I python blir dette:

```python
contract = b"Dette er en superviktig kontrakt for veeldig viktige ting med store ord og uforstaaelige kruseduller." # Kontrakten, som vi får fra kildekoden

m1 = 17 # Tilfeldig tall som vi sender inn til tjenesten, og får signatur 1 tilbake
m2 = bytes_to_long(contract) * inverse(m1, N) % N # Utregning av m2 som vi også sender til serveren. Dette gir oss signatur 2

kombinert_signatur = (sig1 * sig2) % N # Kombiner de to signaturene vi får tilbake
```

Det er også viktig å huske at tjeneste bare tillater HEX input:
```python
m = bytes.fromhex(input("message="))
```
Alt må konverteres til HEX før det sendes. Dette er grunnen til at vi bruker `17` i koden, men sender `11` til serveren. 0x11 == 17.

`helsectf{naar_man_jobber_med_krypto_b0r_man_vite_hva_man_gj0r}`
