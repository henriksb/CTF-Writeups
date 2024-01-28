# Writeup

Dette min writeup på årets CTF utfordring fra HelseCTF. Jeg har ikke alltid de beste løsningne, og ikke alltid alle svarene. Men jeg liker å dokumentere det jeg gjør for å bli bedre.

Oppgaver løst: 38/41 \
Plass: 13/XXX 

## Introduksjon

Denne delen går igjennom introduksjonsoppgavene. Disse oppgavene er ikke spesielt vanskelige, men fine for nybegynnere for å sette seg litt inn i hva en CTF går ut på.

### 1. discord
```
CTF er en sosial sport! Kom og bli med på vår Discord server for å prate med andre deltakere: https://discord.gg/b3zS2QrrU9

Her finner du et gratis flagg. Dette leverer du inn i boksen under.

Som nevnt i reglene på forsiden så vil alle oppgaver følge flaggformatet helsectf{ .. }, hvis ikke annet er oppgitt i oppgaven (det er noen få).

Alle oppgavene i kategorien intro er gratis eller low-effort flagg.
```
#### Løsning
Bli med i Discord kanalen og hent flagget.

**helsectf{men_det_er_jo_lenge_til_Påske!}**

### 2. Kyberkriger
```
Lyst til å være med å avsløre og hindre cyberangrep mot Norge? Vi er på jakt etter dedikerte individer som ønsker å være med på å gjøre internett tryggere. Vår jobb har en betydelig indirekte samfunnsmessig innvirkning som også strekker seg utover helse- og kommunalsektor. Stillingen og mer info finner du her:

https://www.finn.no/job/fulltime/ad.html?finnkode=336880773
```

#### Løsning
Skroll ned i Finn annonsen, så finner du noe rart:
 *xubiusjv{ly_xqh_uwuj_rbkujuqc}*

 Dette er flagget kryptert med ROT-cipher. Finn en [nettside](https://www.dcode.fr/rot-cipher) eller lag et script for å rotere bokstavene.

**helsectf{vi_har_eget_blueteam}**

### 3. Koder
```
Liker du å skrive kode? Er du en nørd med sære interesser for god kode og onelines? Er du lei av at koden din ikke brukes til noe viktig? Vi i Helse- og KommuneCERT ønsker å styrke vårt engineering-team med en eller flere fullstack utviklere. Du vil være med å utvikle løsninger som har stor indirekte samfunnsmessig effekt! For å vite mer kan du lete etter flagg her:

https://www.finn.no/job/fulltime/ad.html?finnkode=336881415
```

#### Løsning
Skroll ned i Finn annonsen igjen, her finner du noe lignende: *aGVsc2VjdGZ7a29kaW5nX2VyX2cweX0=*

Dette er veldig lett å se hva er, da det slutter med et likhetstegn. Finn en [base64 dekoder](https://www.base64decode.org/) og hent flagget.

**helsectf{koding_er_g0y}**

### 4. Hacker
```
Lyst å hacke sykehus og kommuner? Liker du å grave til du treffer fjell? Har du lyst å finne, teste og rapportere om svakheter som kan ha stor indirekte samfunnsmessig effekt? Vi i Helse- og KommuneCERT ønsker å styrke vårt red-team. Se om du tar vår utfordring:

https://www.finn.no/job/fulltime/ad.html?finnkode=336880016
```
#### Løsning
Som de to tidligere oppgavene, finner man problemet på Finn.no igjen. Denne gangen har de laget et assembly program som inneholder flagget. Her kan man kompilere programmet eller finne en [online tjeneste](https://onecompiler.com/assembly/422qyxzn2) som tillater oss å gjøre det. Kjører man koden får man flagget:

**helsectf{statsautorisert_hacker}**

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

### 5. remote
```
I løpet av CTFen er det flere oppgaver som er hostet på en remote server og det krever at du kobler til en "rå" TCP port som går over SSL.

For å koble til hosted challenges har CTFd har dokumentasjon på dette: https://docs.ctfd.io/tutorials/challenges/connecting-to-challenges

Du kan velge å bruke snicat: https://github.com/CTFd/snicat for CLI eller tunnelering/proxy:

sc helsectf2024-2da207d37b091b1b4dff-remote.chals.io
```

#### Løsning
Gratis flagg på https://helsectf2024-2da207d37b091b1b4dff-remote.chals.io/

Koble til med "sc" programmet og hent flagget.

**helsectf{remote_flag_er_best,_ingen_protest!}** 





