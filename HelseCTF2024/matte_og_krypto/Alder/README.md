# Alder
Kari og Ola er to gamle vampyrer.

I dag er Kari 3133713 år eldre enn Ola. Om 5 år vil Kari være 4 ganger eldre enn Ola. Hvor gammel er Kari og Ola i dag?

Flaggformat: helsectf{\<alder kari\>\_\<alder ola\>}

Som eksempel, hvis Kari er 1 år og Ola er 3 år så ville svaret vært helsectf{1_3}. Merk at dette bare var et eksempel for å vise deg hvordan du leverer når du har riktig svar.

## Løsning

For å løse problemet med alderen til Kari og Ola, anvendte vi to kjente forhold og algebra for å sette opp og løse et system av ligninger. Her er detaljene:

**Gitt Forhold**

1. **Første forhold**: Kari er 3,133,713 år eldre enn Ola i dag.

   Dette kan uttrykkes som følger: K = O + 3,133,713, hvor `K` representerer Karis alder og `O` representerer Olas alder.

2. **Andre forhold**: Om 5 år vil Kari være 4 ganger så gammel som Ola.
    
    Dette gir oss følgende ligning: K + 5 = 4 * (O + 5)


Med disse to ligningene har vi et system:\
K = O + 3,133,713\
K + 5 = 4 * (O + 5)


For å løse dette, erstatter vi `K` fra den første ligningen inn i den andre. Dette gir oss: \
O + 3,133,713 + 5 = 4 * (O + 5)

Som forenkles til: \
O + 3,133,718 = 4O + 20

Løser vi denne ligningen for `O` (Olas alder), får vi:

3,133,718 - 20 = 4O - O\
3,133,698 = 3O\
O = 1,044,566


Når vi kjenner Olas alder, kan vi finne Karis alder ved å sette inn verdien av `O` i den første ligningen:

K = 1,044,566 + 3,133,713\
K = 4,178,279

helsectf{4178279_1044566}
