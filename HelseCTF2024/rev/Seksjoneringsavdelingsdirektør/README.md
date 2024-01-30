### Seksjonerinsavdelingsdirektør
```De jobber i feil seksjon, hr. Gustavsen!```

#### Filer
gustavsen (ELF-fil)

#### Løsning
Brukte Ghidra til å dekompilere filen. Her finner vi noe interessant i main-funksjonen:
```c
  local_3c = 0xeefeaafa;
  if (*local_38 == -0x11015506) {
    local_8c = local_38[1];
    local_48 = (char *)xor((long)(local_38 + 2),local_68 - 8,(long)&local_8c);
    puts(local_48);
    free(local_38);
    free(local_48);
    elf_end(local_28);
    close(local_1c);
    return 0;
  }
  free(local_38);
```
Det er litt vanskelig å umiddelbart si hva den gjør, men den printer noe. Dette er også en del av koden som normalt ikke vil bli kjørt. Dette gir mening, da det eneste hintet på oppgaven er at vi kjører i feil seksjon.

For å få kjørt denne koden brukte jeg pwndbg. Her satt jeg et break point på addressen til `local_3c = 0xeefeaafa;`. Dette fant jeg ved å se på den tilsvarende koden i assembly-fanen:

```
001015a6 c7 45 cc        MOV        dword ptr [RBP + local_3c],0xeefeaafa
         fa aa fe ee
001015ad 48 8b 45 d0     MOV        RAX,qword ptr [RBP + local_38]
001015b1 8b 00           MOV        EAX,dword ptr [RAX]
001015b3 39 45 cc        CMP        dword ptr [RBP + local_3c],EAX
```

Etter at et break point er satt, er det bare å trykke `c` (continue) til man verdien `0xeefeaafa` dukker opp. Fortsetter man å trykke continue da vil koden avsluttes. For å hindre dette, må verdien til `RAX` endres. For å gjøre dette skriver man `set $rax=0x11`. Fortsett å gå fremover til flagget dukker opp.

`helsectf{eg_er_i_ein_seksjon_hr_Gustavsen}`