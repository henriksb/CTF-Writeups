# Hvor er Chatboten…?
Dagens oppgave skulle blitt presentert av an feiende flott ChatBot 🤖

Se om du kan finne den der borte 👉

Eller der nede 👇

Kanskje du må trykke på den siste av et dusin funksjonstaster, men du finner den nok til slutt.

## Løsning

Tid brukt: 3 minutter (men begynte sent på dagen)

Inspiser element, så finner du chatbotten i konsollen. Koden til chatboten kan man også finne:

```js
else if (message.includes('kodeord')) {
                console.log('Dagens kodeord er det samme som jeg, og de fleste av mine artsfrender, er – nemlig «' + atob('cGxhZ3NvbQ==') + '».');
```
                
Hvis meldingen inneholder "kodeord" får man flagget.

`ChatBot.snakk("kodeord")`

Dette gir svaret:

`Dagens kodeord er det samme som jeg, og de fleste av mine artsfrender, er – nemlig «plagsom».`

Kodeord: plagsom
