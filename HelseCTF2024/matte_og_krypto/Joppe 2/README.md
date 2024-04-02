# Joppe2

Redd Joppe, død eller levende!

Joppe er igjen låst inn av Adis venner.

Denne gangen er koden delt slik at du trenger 3 av bitene fra gjengen på 5 for å finne koden til safen der Joppe ligger. Koden inneholder også flagget.

Det er ganske store tall, presisjonen må opp og Adi kan ha glemt å bruke modulo her.


## Løsning

Igjen bruker jeg Google til å finne svarene på gåtene, som ga meg koordinatene.

Denne oppgaven er veldig lik "Joppe1", med den vesentlige forskjellen at modulo-operasjonen ikke er brukt her. I stedet er tallet vi mottar ment å direkte inneholde svaret. Oppgaven gir fem ulike koordinater, hvor tre må brukes for å finne løsningen. Valget av hvilke tre koordinater man benytter, er fritt og påvirker ikke resultatet.

Økningen i antall nødvendige koordinater fra to til tre indikerer at vi jobber med en kurve i stedet for en rett linje, som var tilfellet med "Joppe1". Dette antyder at grafen vi arbeider med er ikke-linjær. Ved å beregne skjæringspunktet hvor kurven krysser X=0, finner vi tallet:

`655305480793942574876234195691695898011105414377060925858173`

Konverterer vi det til tekst får vi flagget:

```python
print(long_to_bytes(655305480793942574876234195691695898011105414377060925858173))
>> b'helsectf{muldvarp_er_bra}'
```

