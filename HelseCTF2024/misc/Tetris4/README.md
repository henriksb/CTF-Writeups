### Tetris4
Spill til du har fått renska 5000 linjer på brettet.

#### Løsning
Å spille spillet til 5000 linjer er rensket er bort i mot umulig, så her må man jukse. Koden inneholder også flere funksjoner og sjekker for å hindre at man jukser. Dette betyr at man ikke bare kan sette `linesRemoved` til 5000. Under er funksjonen vi må analysere:
```javascript
function removeLines() {
    var y = 19;
    var linesRemoved = 0;
    while (y > 0) {
        var full = true;
        for (let x = 0; x < 10; x++) {
            if (board[y][x] == 0) full = false;
            else none = true;
        }
        if (full) {
            linesRemoved += 1;
            for (let u = y; u > 0; u--) {
                board[u] = [...board[u-1]];
                board[0] = Array(10).fill(0);
            }
        }
        else y--;
    }
    if (linesRemoved > 4) {
        c();
    }
    else {
        lines += linesRemoved;
        state[0] += linesRemoved;
    }
}
```
Funksjonen `c()` er en funksjon for å hindre juks, men selv om man fjerner hele funksjonen og alle stedene den blir nevnt vil flagget fortsatt ikke dukke opp. La oss kikke på `state[0]`, siden det er her `linesRemoved` går til.

Søker man litt rundt i koden finner man `if(1<state[0]/4e3)`. Denne sjekker om `state[0]/4000` er mer enn 1. Dette ser ut som et ekstra steg for å hindre juks. Denne vil da bli `false` om man prøver å jukse. Hvis vi endrer denne til å bli `true`, vil vi kunne jukse. Vi kan da endre den til `if(1<2)`, og så prøve å sette `linesRemoved` til 5000. Dette gir oss flagget.

`helsectf{nocheat}`
