### Claim_in_mail
Du har fått en e-post med et html-vedlegg. Det er vel bare å åpne det?

Tips: Nøst opp i angrepskjeden. Finn ut hva den forsøker å kjøre. Målet er å finne siste tilgjengelig steg i kjeden.

I god stil er oppgavefilen pakket i en kryptert zip. (passord infected)

#### Filer
Oppgave.zip

#### Løsning
Inne i `Oppgave.zip` finner vi en fil som heter `Claim_3456.vhd`. Jeg åpnet denne opp i Autopsy og hentet ut alle filene som så interessante ut. Her finner vi blant annet et program som heter `crossbar.exe`. Etter å ha kikket litt på det ser det ut som om det er et dotnet program. Dette betyr at vi enkelt kan se på koden. Jeg åpnet exe filen i IlSpy og fant at `giefKey` var et argument. For å få flagget kjører man exe-filen med det argumentet.

`helsectf{if_it_qaks_like_a_bot_6ebd7e86fa5a82fb062800f9529fede402ab4b758453ee1456197754ca051145}`