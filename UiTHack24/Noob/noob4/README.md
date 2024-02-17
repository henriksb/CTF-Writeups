# Noob4
Our trip through space and time seems to have messed with the future, and now we cannot access our flag! (There might be a space on the end of the flag...)

You can connect to the server with the following command: nc uithack.td.org.uit.no 6003

The username is noob4

The password is the flag from noob3

nc uithack.td.org.uit.no 6003

## Løsning
Denne oppgaven er litt mer utfordrenes, da man ikke bare kan kjøre `cat` på `flag.txt`. Grunnen til dette er at filen er `-flag.txt`, som betyr at `cat` kommandoen tror at dette er et argument. For å unngå dette kan man bruke `--` for å si at det ikke er fler argumenter, men det er fortsatt et problem; det er to filer med samme navn. Hvis vi ser litt mer nøye på det og bruker kommandoen `ls -1b` kan vi se at de faktisk har forskjellige navn. Filen med innhold heter `-flag.txt\`. Da brukte jeg bare wildcard symboldet (*) og fikk flagget med følgende kommando:

`cat -- -flag.txt*`

`UiTHack24{d4sh_31337}`