### pass_or_fail
.bat - filer kan gjøre ganske mye. Denne bat-filen vil ikke kjøre noe skummelt om du kjører den. Finn ut hva den gjør. Evt hva du kan mate den med (input) for å få ønsket resultat.

Flagget gjemmer seg i en pass, ikke en fail.

Passord for zip-fil er standard (infected).

#### Filer
pass_or_fail.zip

#### Løsning
Åpner man denne bat filen ser man ikke noe annet enn kinesiske tegn, som tyder på at den er obfuskert med en annen encoding. Jeg fant et [python script for å deobfuskere batch filer](https://github.com/DissectMalware/batch_deobfuscator) og brukte det. Dette ga meg en lesbar kode:

```bat
@echo off
set "饿饿尔艾=wrUnsT7NBeCfiljYRb5cPF2oQ8SWZzG@VJpvXxO6K3HI LadgAqDmu14h=MEkty09"
@set "斯尔色斯=Kt@4oE2uzLIZ80qiR1YpOldD SjNe7bWskfvUMCwVBnrGgFHamPJhxXAyQ536c9=T"
@set "饿阿豆豆=ybVIQN=SoEOikuHCcfa2 LhB3KUA6rzXxY0Dw7nJg4sM9tjG85d1ZqePlWRv@FTpm"
@set "尔色爱德=NaY35kTOpHZ@2E0hI=yrxjm SUbKF6eiCW7R9fslt8wJuzdoDLA1Gv4nQgMXVPcBq"
@set "斯尔贝贝=RzxkNpCdKhS3@2efquTcowElvU8W9rLHVa 6AZDG7Q0Yy5JijnFO4MPbgXmBtI1s="
for /l %%y in (1 1 1) do @echo off
if 1 EQU 1 set "abc2=https://youtu.be/YZf0Q-v3u-k?feature=6e6569746865722069732074686973"
for /l %%y in (1 1 1) do set "abc3=https://youtu.be/3xYXUeSmb-Y?feature=54686973206973206e6f742074686520666c6167"
if 46 EQU 0 (@exit) else set "abc4=G@nd@lf"
if 1 EQU 1 set "abc1=https://youtu.be/qybUFnY7Y8w?feature="
if 1 LsS 109 set "abc7=explorer.exe"
if 1 EQU 1 if not "" equ "" goto usage
for /l %%y in (1 1 1) do goto end
:usage  lliiliiilil   llililllili
if 1 LsS 109 set "abc5=68656c73656374667b746869"
if 1 LsS 109 if == (set "abc6=735f325f7368616c6c5f706173737d"
if 1 LsS 109 set "abc7="
) else (start )
if 1 LsS 109 start 
if 1 LsS 109 exit
:end  lilllillill   liillllllil
for /l %%y in (1 1 1) do start 
```

Her kan vi se mye base64 og HEX data. Gjør vi HEX dataen om til tekst får vi flagget.
```bat
if 1 LsS 109 set "abc5=68656c73656374667b746869" & :: helsectf{thi
if 1 LsS 109 if == (set "abc6=735f325f7368616c6c5f706173737d" & :: s_2_shall_pass}
```

`helsectf{this_2_shall_pass}`
