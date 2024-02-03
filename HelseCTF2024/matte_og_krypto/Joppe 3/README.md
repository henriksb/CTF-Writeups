### Joppe3
Redd Joppe, død eller levende!

Koden blir igjen delt opp mellom de 5 og man må løse minst 3 oppgaver for å finne koden til låsen.

Men denne gangen hadde Adi sovet dårlig, og noe gikk galt. Presisjonen på tallflytsoperasjonene ble noe unøyaktig, også mumlet Adi noe om at finner du x, finner du koden.

Igjen er det ganske store tall, presisjonen må opp og Adi har igjen glemt å bruke modulo her.

#### Løsning
Gåtene blir Googlet, som vanlig.

Denne utfordringen viste seg å være litt forvirrende i starten. Jeg identifiserte raskt verdien av X, og fulgte den samme tilnærmingen som i den tidligere oppgaven, "Joppe2". Jeg beregnet først skjæringspunktet hvor X=0, noe som resulterte i et tall. Dette tallet ble så konvertert til tekst: `x=323454343235`. Ved å justere X-verdien til å matche dette tallet, endte jeg bare opp med tull.

Etter noen forsøk innså jeg at det ikke var mulig å bruke tre vilkårlige koordinater fra de fem gitt. Ved å eksperimentere med alle mulige koordinatkombinasjoner, endte jeg opp med tre forskjellige X-verdier:

```
x=323454343235
x=323454343234
x=323454343233
```

Ved å beregne og konvertere punktet hvor kurven krysser disse tre spesifikke X-verdiene til tekst, viste det seg at riktig løsning var `x=323454343233`. Dette ga meg et tall som ble konvertert til `helsectf{Jimmy_Ekelune\x15`. Det kan ha vært noen nøyaktighetsproblemer i min beregning, men et kjapt Google-søk ledet meg til "Jimmy Ekelund", kjent fra TV-programmet "Redd Joppe, død eller levende".

`helsectf{Jimmy_Ekelund}`
