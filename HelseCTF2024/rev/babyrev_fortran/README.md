### babyrev_fortran

En babyrev husker gamle fortellinger fra sin bestefar som programmerte i et litt utdatert programmeringsspråk. Heldigvis kom det en senere revisjon på 90-tallet som er noe enklere å bruke.

Greier du å printet ut flagget i klartekst?


#### Filer
babyrev_fortran (ELF-fil)

#### Løsning
Kjør programmet, så får man teksten:
```flag=gemredsf|k3oFe`r1E2n`e02j_qqoh`MNdR8d_j^Fpqts`n`80~```

Her kan man fort se at deler av "helsectf" er korrekt. Ser man nærmere på dette så finner man mønsteret +1,0,-1. Altså, bokstaven etter, samme bokstav, og bokstaven før. For å løse dette kan vi lage et script til å fikse bokstavene:

```python
flagg = "gemredsf|k3oFe`r1E2n`e02j_qqoh`MNdR8d_j^Fpqts`n`80~"

svar = ""

for i, char in enumerate(flagg):
    offset = (1, 0, -1)[i % 3] # Veksle offset med 1, 0 og -1
    svar += chr(ord(char) + offset) # Gjør om til asciitall, legg til   offset og gjør om til bokstav.

print(svar)
>> helsectf{l3nGe_s1D3n_f01k_progaMMeR7e_i_Fortran_90}
```
