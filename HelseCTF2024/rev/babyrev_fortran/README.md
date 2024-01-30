### babyrev_rust
```
En babyrev er litt Rust(en) i programmering. Hen har programmet inn et flagg i kildekoden, kompilert det til en binærfil (se vedlagt fil) men har så greid å mistet kildekoden. Om hen bare hadde skrevet ned argumentet. Kan du finne flagget og levere det inn?

Reven har noen vage minner om at det kan være et par hint i filen som kan hjelpe en ivrig REverser i å finne flagget.
```

#### Filer
babyrev_rust (ELF-fil)

#### Løsning
For å løse denne ble pwndbg brukt. Etter litt graving i `main` fant jeg funksjonene: `lang_start` og `lang_start_internal`. Gikk inn i de og fortsatte til jeg fant ```}!gitkir_tvitaler_remir_tsur_ksar{ftcesleh'``` som blir reversert til:

```helsectf{rask_rust_rimer_relativt_riktig!}```

Takk til [Aadlei](https://github.com/Aadlei) for hjelp med denne oppgaven.

Man kan også finne to hint i filen:

1. Kan det være en enklere måte finne å flagget på enn å reversere main?? Think kanskje jeg kan bruke en debugger.
 
2. Om jeg bare hadde husket hvordan jeg bruker en tracer.