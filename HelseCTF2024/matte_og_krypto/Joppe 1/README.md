# Joppe1
Redd Joppe, død eller levende!

Ola har en lei tendens til å miste muldvarpen sin, Joppe. Denne gangen er den blitt kidnappet av Adi Shamir og hans venner. Adi har låst den inn i safen med en kode som ingen helt vet.

De tre vennene har delt koden mellom seg på en slik måte at du trenger to av bitene for å kunne rekonstruere koden til safen.

De går med på å gi deg sin bit hvis du kan løse deres gåte.

Bruk endepunktet under for å prøve deg på gåtene.

Om du bruker du Adis metode eller ikke så finner du koden på null.


## Løsning
Når man kobler til serveren man får i oppgaven må man svare på tre forskjellige gåter. Disse brukte jeg Google til å finne svaret på. For hver gåte man løser får man X og Y koordinater tilbake.

Prosessen involverer en teknikk kjent som "Shamirs hemmelighetsdeling". Dette er en metode for å dele og senere rekonstruere en hemmelighet, hvor man trenger et visst antall andeler (i dette tilfellet koordinatsett) for å finne tilbake til den opprinnelige hemmeligheten. Selv om antallet nødvendige andeler kan variere, er den underliggende ideen at man skal finne et punkt hvor linjene krysser X-aksen ved X=0. Ved å identifisere Y-verdien på dette punktet, kan man avsløre hemmeligheten. Dette kan oppnås gjennom matematiske beregninger eller ved å tegne og analysere grafene av de oppgitte koordinatene. Følgende Python kode ble brukt til å finne verdien:

```python
from sympy import symbols, solve
from numpy.polynomial.polynomial import Polynomial

# Coordinates provided
points = [(-500, 1229), (500, 2229), (1000, 2729)]

# Fit a linear polynomial to these points
p = Polynomial.fit([point[0] for point in points], [point[1] for point in points], 1)

# The polynomial is of the form ax + b, we need to find the value at x=0, which is simply b
safe_code = p.convert().coef[0]  # Convert to standard form and get the constant term

print(safe_code)
#1729
```

Vi finner da tallet, som er `1729`. Sender vi dette inn til serveren får vi flagget tilbake.

`helsectf{ved_x_null_er_alt_gull}`
