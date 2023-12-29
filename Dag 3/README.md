# Redacted

## Filer
📎 Mitt utpressingsbrev.docx

📎 huskeliste.txt.enc

## Oppgavetekst
Det er krise! Filene på alvemaskinene har blitt kryptert, og vi har ingen backups tilgjengelig!

På nissens skrivebord fant vi det vedlagte brevet, sammen med en kryptert fil.

Det er ubeskrivelig viktig at vi får åpnet denne filen igjen umiddelbart, da Jule NISSEN ikke klarer å huske innholdet!

- Mellomleder

## Løsning

Åpne Word-dokumentet og fjern den svarte boksen merket med 'REDACTED'. Bak denne skjuler nøkkelen seg. Bildet i dokumentet indikerer at AES-CTR-kryptering er brukt, og at nøkkelen i tillegg er sikret med ROT-13-kryptering. Nederst i dokumentet finner vi også Initialiseringsvektoren (IV). Gitt nøkkelens lengde på 48 tegn, kan vi slutte at AES-192-kryptering er anvendt. Det er viktig å merke seg at IV må være i HEX-format. Ved å kombinere all denne informasjonen, kan vi konstruere følgende kommando for å dekryptere filen:

```openssl enc -aes-192-ctr -d -in huskeliste.txt.enc -out decrypted_file -K dda2846b010a6185b5e76aca4144069f88dc7a6ba49bf128 -iv 4867746e617466497278676265313233```

Svar: KRIPOS{Husk å se etter spor i snøen!}
