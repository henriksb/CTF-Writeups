# Alvesortering

## Filer
📎random_text.bin

## Oppgavetekst
De strenge alvene har skrevet ned et julekodeord, men i den ivrige sorteringen av pakker har det skjedd en horribel feil og alt er blitt rot! Ordet har blitt borte i det som ser ut som et virrvarr av tilfeldig tekst! Nå trenger de hjelp til å gjenfinne ordet. De har null peiling på hvor langt ordet er. Kan du å gjenfinne ordet?

- Mellomleder

## Løsning
"Sortering" er hintet. I filen er det rundt 1000 "null" tegn. Splitt teksten ved null-tegnet og sorter alle elementene etter lengde. Her finner man flagget som første bokstaven av linjene.

Svar: PST{julenisseStreng0Alv}
