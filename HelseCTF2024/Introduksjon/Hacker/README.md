### Hacker
`
Lyst å hacke sykehus og kommuner? Liker du å grave til du treffer fjell? Har du lyst å finne, teste og rapportere om svakheter som kan ha stor indirekte samfunnsmessig effekt? Vi i Helse- og KommuneCERT ønsker å styrke vårt red-team. Se om du tar vår utfordring:

https://www.finn.no/job/fulltime/ad.html?finnkode=336880016
`
#### Løsning
Som de to tidligere oppgavene, finner man problemet på Finn.no igjen. Denne gangen har de laget et assembly program som inneholder flagget. Her kan man kompilere programmet eller finne en [online tjeneste](https://onecompiler.com/assembly/422qyxzn2) som tillater oss å gjøre det.

```assembly
global _start

section .text
    global _start

section .data
    hemmelig db 0x2a,0x27,0x2e,0x31,0x27,0x21,0x36,0x24,\
                0x39,0x31,0x36,0x23,0x36,0x31,0x23,0x37,\
                0x36,0x2d,0x30,0x2b,0x31,0x27,0x30,0x36,\
                0x1d,0x2a,0x23,0x21,0x29,0x27,0x30,0x3f,\
                0x48

_fix:
    mov eax, [hemmelig + ecx]
    xor edi, edi
    add edi, 0x41
    add edi, 1 
    xor eax, edi
    mov [hemmelig+ecx], al

    add ecx, 1
    mov esi, 0x21
    cmp ecx, esi
    jle _fix

    ret

_start:
    xor ecx, ecx    
    call _fix
    mov eax, 4
    mov ebx, 1
    mov ecx, hemmelig
    mov edx, 0x21
    int 0x80

    mov eax, 1
    xor ebx,ebx
    int 0x80 
```
Kjører man koden får man flagget:

`helsectf{statsautorisert_hacker}`
