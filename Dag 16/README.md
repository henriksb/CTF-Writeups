# Invasjon

## Filer
📎aksjon_2023.zip

## Oppgavetekst
Gjennom temmelig hemmelige innhentingsmetoder har vi fått tak i det vedlagte dokumentet som avslører den egentlige hensikten bak løsepengeangrepet: Sydpolare aktører planlegger å invadere Nordpolen for å stoppe julen én gang for alle!

I dokumentet nevnes det at aktørene har plantet deep-cover agenter i blant oss, og at de har hemmelige koder for å etablere kontakt med disse. Analyser materialet og se om du klarer å avsløre de hemmelige kodene slik at vi kan få disse agentene på kroken!

I mellomtiden iverksetter vi umiddelbare mottiltak for å stanse invasjonen.

- Tastefinger

## Løsning
Jeg gikk gjennom alle branches og fant en interessant branch med navnet "ikke-merge-før-julaften". Om man sjekker den ut med kommandoen ```git checkout ikke-merge-før-julaften``` henter den ut en fil med navnet "feltagenter_kontaktmanual.md". Denne filen inneholder:
```# Eksfil av feltagenter

Våre deep-cover feltagenter har blitt instruert i å respondere på følgende koder.

Bruk disse for å initiere kontakt ved eksfil etter vellykket operasjon, eller ved ekstraordinært behov ellers.

## Koder

- Agent "Julie Bånd": KODE_PLACEHOLDER_1
- Agent "Solid Sankt": KODE_PLACEHOLDER_2
- Agent "Jollyson Bål": KODE_PLACEHOLDER_3
```
Shell skriptet ```/aksjon_2023/.git/hooks/pre-merge-commit``` inneholder flere base64 strenger som blir printet i konsollen om filen "feltagenter_kontaktmanual.md" finnes. Vi kan da manuelt dekode alle base64-strengene, eller kjøre skriptet. Hvis vi kjører skriptet vil kodene i "feltagenter_kontaktmanual.md" bli destruert. For å fikse dette må vi lese og forstå skriptet. For å hindre selv-destrueringen må vi skrive kommandoen ```export DISABLE_SELF_DESTRUCT=1```. Vi kan da kjøre skriptet, og "KODE_PLACEHOLDER" vil bli erstattet med flagget.

Svar: KRIPOS{Flagg i alle kriker og kroker}
