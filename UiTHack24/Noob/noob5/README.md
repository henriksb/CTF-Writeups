# Noob5
Get the flag to join the galactic elite!

You can connect to the server with the following command: nc uithack.td.org.uit.no 6004

The username is noob5

The password is the flag from noob4

nc uithack.td.org.uit.no 6004

## Løsning
I denne oppgaven har vi ikke tillatelse til å lese flagget. Den eneste brukeren med tillatelse er `elite`. Går vi tilbake ett hakk med `cd ..` ser vi at det er to mapper der, en med navnet `ctf`, og en annen med navnet `elite`. Går vi inn i `elite` mappen finner vi en fil som heter `cat`. Denne er også eid av `elite`. Vi kan kjøre denne filen, som betyr at vi kan bruke den på flagget.

```sh
cd ../elite
./cat ../ctf/flag.txt
```

`UiTHack24{7h3_n00b_g4l4ct1c_31337}`