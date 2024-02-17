# Noob3
Oh no! Someone deleted flag.txt from our system, and our spaceship is broken, so we are not able to go back in history to retrieve it.

You can connect to the server with the following command: nc uithack.td.org.uit.no 6002

The username is noob3

The password is the flag from noob2

Read up on how Linux stores the bash history to get the flag.

nc uithack.td.org.uit.no 6002

## Løsning
Her igjen bruker vi `ls -alt` til å finne alle de skjulte filene. Her finner man filen `.bash_history`. Denne filen inneholder historikken til terminalen. For å finne flagget kjører man `cat` på denne filen. Her finner man flagget:

`echo "UiTHack24{1337_t1m3_tr4v3ll3r}" > flag.txt`