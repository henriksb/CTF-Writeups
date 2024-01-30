### Null pointer
Utvikler Per Ointer trenger av og til å kjøre python-programmer på webserveren sin. Derfor har han laget en veldig enkel webtjeneste for å sende inn python-programmer og returnere output:

Eksempelkjøring av program: curl 'http://server/?program=print(repr(repr))'

For å hindre misbruk er kun 10 forskjellige tegn tillatt i python-programmet: pointer(*)

Dessverre viser det seg at dette ikke er godt nok. Hent ut flagget i fila 0 i current directory.

#### Løsning
Her blir vi begrenset til tegnene i `pointer(*)`, men med en gang ser man at vi mangler noen tegn. Stegene for å løse denne er:

1. Finn en måte å få tallet 0 på
2. Gjør tallet null om til string
3. Åpne opp filen "0"
4. Print innholde tilbake til oss

Det er flere hint i denne oppgaveteksten som er veldig nyttige.

1. For å få tallet null kan man bare skrive `int()`.
2. Hintet i oppgaveteksten er bruken av `repr`. Vi kan bruke dette til å gjøre tallet vårt om til en string. 
3. `open()` blir selvfølgelig brukt til å åpne filen.
4. Prøver vi nå å printe innholdet vil vi kun printe objektet, ikke innholdet. Dette er fordi vi mangler `.read()`. En annen måte å løse dette på er å bruke en pointer (*), som det var hintet til i oppgaveteksten.

Setter vi dette sammen får vi `print(*open(repr(int())))`.

`helsectf{z3r0_p0inters_g1ven}`