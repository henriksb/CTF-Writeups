### Konvertere
```python
For å konvertere mellom store tall og strenger anbefales det å bruke pycryptodome i Python. Denne kan installeres med pip install pycryptodome.

Vi bruker denne i f.eks. kryptooppgaver med RSA for å gå fra byte-strenger til tall for å gjøre RSA operasjoner, og tilbake. Dette er brukt i RSA oppgaven kontraktsignering.

Jeg har skjult et flagg som et tall:

>>> from Crypto.Util.number import long_to_bytes, bytes_to_long   
>>> flag = bytes_to_long(b"helsectf{??? ... ???}")
>>> print(flag)
9999168102934914777774346849293018679871929920575661949

For å konvertere tilbake til bytes kan du bruke print(long_to_bytes(<tall>))
```
#### Løsning
Her får vi en ganske grei beskrivelse på hvordan man får flagget:

```python
from Crypto.Util.number import long_to_bytes, bytes_to_long   
flag = long_to_bytes(b"9999168102934914777774346849293018679871929920575661949")
print(flag)
```
Dette gir oss flagget:

`helsectf{bytes_to_long}`