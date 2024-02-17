# Rapid Encryption
Those pesky aliens keep sniffing our messages and stealing our supplies! Luckily I have come up with a way to encrypt our messages so that they won't know where our supplies are located. I had to improve the encryption time of the algorithm, but I'm sure it makes no difference...

## Filer
encrypt.py \
out.txt

## Løsning
Dette er en RSA oppgave, som man kan se i `out.txt` filen. Her ser man en `ct`, `n`, og `e` verdi. Disse kan man bruke til å få flagget. Jeg brukte [dcode.fr](https://www.dcode.fr/rsa-cipher) til å dekryptere.

`UiTHack24{3ncryp7i0n_g0es_brrrr}`