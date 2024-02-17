# Hidden Covenant Info
The covenant is slowly advancing to New Mombasa. We managed to catch a photo they sent in their communications channel, however we do not have their location. We believe the covenant is communicating with photos. Your mission Rookie, is to figure out what their location is; by finding the hidden information within the photo.

## Filer
Yanmee.jpg

## Løsning
Brukte steghide og fant en tekstfil med navnet `new_flag.txt`. Denne filen inneholdt `UiTHack24{Airview` og massevis av whitespace. Den siste delen av flagget var whitespace encoding, som jeg dekodet med [dcode.fr](https://www.dcode.fr/whitespace-language.)

`UiTHack24{Airview_outpost}`