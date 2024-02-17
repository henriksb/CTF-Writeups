# Admin Access
You have to inflitraite the admin area of this website to get the flag. But how do you access it?

https://uithack.td.org.uit.no:3000

## Løsning
Denne oppgaven er en SQL-injection oppgave. Vi får også et hint i tittelen om hvilket brukernavn vi skal bruke (admin). For å logge inn bruker vi `admin` som brukernavn, og for å unngå passordet må vi konstruere en SQL kommando. Dette er kommandoen jeg brukte:

`'or 1=1 --`

Den første `'` bruker vi for å avslutte den første SQL kommandoen.\
`or 1=1` bruker vi for å få `true`, for at passordet skal være sant.\
Den siste delen, `--` bruker vi for å kommentere ut den siste delen som vi ikke ser.

`UiTHack24{SqL_1nj3ct10n_1s_4m4z1ng}`