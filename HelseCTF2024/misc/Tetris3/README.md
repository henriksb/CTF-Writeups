### Tetris3
Nede i horisonten, under fjell, snø og terreng ligger det et flagg.

#### Løsning
Oppgaveteksten hinter om at flagget ligger gjemt under bakgrunnen. Hvis vi ser på koden finner vi:
```javascript
function drawFrame(frame) {
    var imageData = ctx.getImageData(0, 0, width, height);
    var fb = imageData.data;
    drawSky(fb);
    drawTerrain(fb);
    drawBoard(fb);
    if (currentMode == 'WELCOME' || currentMode == "GAMEOVER") drawBitMap(fb, 110, 20, title);
    if (currentMode == 'PAUSE') drawBitMap(fb, 105, 80, paused);
    if (currentMode == 'GAMEOVER') drawBitMap(fb, 53, 70, gameover);
    if (currentMode == 'CHEATER!') drawBitMap(drawBitMap(fb, 86, 60, cheat));
    drawBirds(fb, frame);
    ctx.putImageData(imageData, 0, 0);
}
```
Ved bruk av hintet som sier "under terreng", kan vi fjerne `drawTerrain(fb)`, som gir oss flagget.

`helsectf{himmelferd}`