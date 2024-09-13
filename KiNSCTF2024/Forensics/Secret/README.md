# Secret

## Oppgavetekst

Analyser zip-filen og finn flagget.

Oppgi svaret i formatet: ctf{svar}

NB! Merk at du må oppgi flagget med klammeparantes!

## Løsning

Inne i den passordbeskyttede ZIP-filen fant jeg en passordliste kalt "darkc0de.txt", samt en README.md fil og et bilde. Alt dette ble hentet fra en GitHub repository: https://github.com/danielmiessler/SecLists. Ved å matche datoene i ZIP-filen fant jeg de eksakte filene som var brukt.
Deretter genererte jeg en ny ZIP-fil med et identisk oppsett og noen identiske filer.  zipinfo -v secret.zip  ble brukt for å verifisere at filene var komprimert likt.  Kommandoen jeg brukte for å generere ZIP-filen er: `zip -9 newsecret.zip README.md SecLists.png darkc0de.txt`.

Etter filen var klar brukte jeg verktøyet pkcrack for å dekryptere den orginale filen: `pkrack -C secret.zip -c README.md -P newsecret.zip -p README.md -o flagg.zip` 