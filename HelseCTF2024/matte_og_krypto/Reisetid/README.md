### Reisetid
Kari og Ola bor 150km fra hverandre og skal møtes for å ta en kaffe. Kari kjører kl 1200, og ville brukt 3 timer om hun måtte kjøre hele lengden på 150km. Ola kjører kl 1300, og ville brukt 5 timer om han måtte kjøre hele lengden på 150km.

Hva er klokka når de møtes, og hvor langt i meter har Kari kjørt?

Flaggformat: helsectf{\<tid 4tall\>\_\<lengde i meter\>}

Som eksempel, hvis de møtes kl 1201 og Kari har kjørt 11km så vil svaret være "1201_11000". Merk at dette bare var et eksempel for å vise deg hvordan du leverer når du har riktig svar.

#### Løsning
1. **Karis Forsprang på Grunn av Olas Forsinkelse:**  
   50 km/t * 1 t = 50 km

2. **Gjenstående Avstand når Ola Starter:**  
   150 km - 50 km = 100 km

3. **Kombinert Hastighet:**  
   50 km/t + 30 km/t = 80 km/t

4. **Tiden det Tar før de Møtes etter Ola Starter:**  
   100 km / 80 km/t = 1.25 timer

5. **Total Tid Kari Kjører:**  
   1 t + 1.25 t = 2.25 timer

6. **Avstand Kari Kjører:**  
   2.25 t * 50 km/t = 112.5 km

7. **Møtetidspunkt:**  
   12 timer + 2.25 timer = 14.25 timer = 14:15 klokkeslett

8. **Karis Kjøreavstand i Meter:**  
   112.5 km * 1000 = 112500 meter

`helsectf{1415_112500}`