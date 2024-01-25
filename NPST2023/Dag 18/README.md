# Melding fra antikken

## Filer
📎melding.txt

## Oppgavetekst
I riktig gamle dager hadde NISSEN flere regionskontor spredt rundt i verden. Disse kontorene fungerte både som mottak for ønskelister og distribusjonssenter for gaver. Da som nå var det ikke alle som oppførte seg like pent fram mot jul, og ifølge historiebøkene var spesielt organisasjonen PERSIUS (ledet av den onde Dr. Xerxes) stadig vekk på spion- og toktforsøk mot ett av NISSENs regionkontor. På sitt verste var det angivelig hele 300 alvebetjenter i sving for å forsvare gaver og ønskelister. De særs tapre alvene til tross, NISSEN var reelt bekymret for at viktig informasjon og gaver skulle havne på avveie. Siden den gang har derfor all julesensitiv informasjon blitt kryptert.

Takket være noen alvorlige logistikkproblemer (og muligens en streik eller to) har plutselig en slik gammel melding dukket opp. Julelovens paragraf §133-syvende ledd er imidlertid krystallklar

``
Enhver julesensitiv informasjon må analyseres og vurderes før den avgraderes høytid.
``

Imidlertid er det ingen av Alvene som aner hvordan denne gamle meldingen skal leses. Kan du hjelpe dem?

- Mellomleder

## Løsning

Oppgaven inneholdt hint som pekte mot filmen "300". Dette førte meg til å søke etter spartanske krypteringsmetoder på nettet, hvor jeg oppdaget "Scytale Cipher". Med denne informasjonen utviklet jeg et Python-script for å gjennomføre en brute-force-metode på alle mulige kombinasjoner av denne krypteringen, noe som til slutt avslørte koden. Jeg oppdaget senere at nettsiden https://www.dcode.fr/scytale-cipher også kan benyttes for å dekryptere denne typen kode.

Svar: pst{var_julenissen_kong_leonidas}
