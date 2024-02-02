### Prikker
En TV skjerm har klikket helt og viser bare prikker i ulike farger. Hvis man ser godt etter kan man kanskje se en hemmelig melding, spesielt hvis man finner den riktige fargen!

#### Filer
prikker.zip

#### Løsning
Vi mottar et bilde av en GIF på 4000 bilder. Denne GIF-en viser én ny prikk for hvert bilde.

![prikk](prikker.gif)

For å finne flagget på denne må vi fjerne den svarte bakgrunnen og legge sammen alle bildene. Dette kan bli gjort med `imagemagick`.

Først, splittet jeg opp GIF-en til 4000 bilder:\
`ffmpeg -i ../prikker.gif prikk-%d.png`

Etter det fjernet jeg den svarte bakgrunnen:\
`ls prikk-*.png | while read filename; do convert $filename -transparent black $filename; done`

La sammen bildene:\
`ls prikk-*.png | while read filename; do convert $filename prikk-1.png -gravity center -composite prikk-1.png; done`

Og fikk bildet:
![resultat](prikk1.png)

Det er litt vanskelig å lese hva som står det, da man sikkert skal fjerne alle prikkene som ikke er røde. Men hvis man studerer bildet litt og bruker litt kreativitet kan man finne flagget.

`helsectf{en_prikk_kan_ha_mange_farger!}`