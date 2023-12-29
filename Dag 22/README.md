# Gaveliste-endring

## Filer
📎 ALARM_JULESOC.zip

## Oppgavetekst
Hei Henriksb,

JULESOC har fått en alarm fra informasjonssystemet tilknyttet NISSENS gavelager på VALøya i Tromsø. Alarmen handlet om en uautorisert modifikasjon i databasen som styrer inventaret til lageret, og JULESOC har sendt oss databasefilene slik de forekom på tidspunktet alarmen gikk.

Har du mulighet til å sjekke ut filene og finne ut hvilken rad som er blitt modifisert?

📎 ALARM_JULESOC.zip

Returner UUID til den modifiserte raden, f.eks. PST{6eab374e-735f-416e-bcc6-81b4b8dfc7a9}

## Løsning
Åpnet i DB Browser og sortere "quantity". Her så jeg en gjenstand med "quantity" på 0. Dette var visst flagget.
```
| UUID				                         |      giftname      | quantity
| 9da1b2a6-5a52-41ec-8bf0-32381e054db7 | Nano Jade Mindflex |    0
```

PST{9da1b2a6-5a52-41ec-8bf0-32381e054db7}
