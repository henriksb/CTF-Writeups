# Et påskemysterie...
I natt har det vært innbrudd på hjemmekontoret til vår CTO, Tomas. Merkelig nok var det eneste som ble ser ut til å ha forsvunnet, en signert utgave av boken:

Inga Strümke – Maskiner som tenker
Tomas mistenker at en perifer bekjent teknologiskeptiker står bak ugjerningen. Inntrengeren etterlot to spor.

Spor 1: Tegningen på veggen
Figuren under var, omhyggelig tegnet på veggen ved siden av bokhylla der det nå mangler én bok.


Spor 2: Notatboken
Ved siden av bokhyllen lå det henslengt en notatbok. De fleste sidene var blanke, men følgende skriblerier var å lese.

158.39.129.53 \
Hartmark & Stangeland, 1956 \
Elektronisk databehandling \
67 - 17 - 7 - 8 \
6 - 13 - 7 - 2 \
18 - 7 - 7 - 1 \
57 - 11 - 9 - 1 \
66 - 11 - 8 - 8 \
69 - 30 - 7 - 1 \
40 - 1 - 1 - 1 \
12 - 10 - 4 - 9 \
3 - 28 - 1 - 13 \
40 - 2 - 4 - 8 \
58 - 20 - 3 - 1 \
52 - 1 - 5 - 23 \
8 - 2 - 1 - 6 \
Undersøk sporene, og se om du ved å slå alt sammen kan finne ut hvem som står bak, eller i det minste komme frem til dagens kodeord...

## Løsning

Tid brukt: 11 minutter.

Det er et bilde i oppgaveteksen, åpner man dette har det en rar URL: https://kodekalender.novacare.no/luke3/fvqr_yvawr_beq_obxfgni.jpg

Det ser ut som om det kan inneholde en tekst kryptert med ROT-13. Dette viste seg til å stemme.

fvqr_yvawr_beq_obxfgni = side_linje_ord_bokstav

Notatblokken begynner med en IP: `158.39.129.53`. Åpner man denne nettsiden får man tilgang til boken som er nevnt i teksten.

```
side_linje_ord_bokstav
67 - 17 - 7 - 8 t
6 - 13 - 7 - 2  a
18 - 7 - 7 - 1  s
57 - 11 - 9 - 1 k
66 - 11 - 8 - 8 e
69 - 30 - 7 - 1 n
40 - 1 - 1 - 1  s
12 - 10 - 4 - 9 p
3 - 28 - 1 - 13 i
40 - 2 - 4 - 8  l
58 - 20 - 3 - 1 l
52 - 1 - 5 - 23 e
8 - 2 - 1 - 6   r
```

Kodeord: taskenspiller
