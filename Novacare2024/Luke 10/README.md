# Novacare 10 år!
I forbindelse med at Novacare fyller 10 år i år, faktisk akkurat i dag, har vi valgt å ta grep for å bedre hverdagen for våre utviklere. Den stillesittende arbeidshverdagen som har vært en realitet for mange, kan føre til en rekke utfordringer og plager.

Nyere forskning viser at i en vanlig samtale kan kroppsspråk stå for så mye som 70% av budskapet. Vanligvis når utviklere skriver kode, er dette informasjon som bare går tapt. Litt forenklet kan vi si at vi til nå har operert med kun 30% utnyttelse av kapasiteten vår!

Fra og med i dag innfører vi obligatorisk bruk av kroppsspråk, for alle utviklere i alle prosjekter. I en innkjøringsfase vil det kun være krav om fem minutters kroppsspråk per time, men planen er å øke gradvis etter hvert som de ansatte blir mer komfortable med å uttrykke seg via kroppsspråk. På litt sikt er målet å fjerne tastaturene fullstendig.

Pålagt bruk av kroppsspråk vil ikke bare føre til økt bevegelse og mosjon i arbeidstiden, men det vil også føre til mer variasjon i arbeidsstilling. Samlet vil dette drastisk redusere fysiske plager forårsaket av stillesitting. Andre fordeler vil antagelig kunne være bedre helse, lavere sykefravær, mer overskudd og større arbeidsglede.

Dagens oppgave er på en måte en blanding av de to foregående oppgavene. Ta en kikk på kroppsspråket i videoen under, og se om du kan se hvilket kodeord vi skal frem til…

https://www.youtube.com/watch?v=y3p8DwkeaAQ

**Oppdatering 1. april kl 21:40:**
Et sted i koden skrives det ut <<<<<<<, der det hadde vært mer passende med <<<<<. I vår implementasjon av brainfuck interpreteren har ikke dette noen betydning, siden cellepekeren ikke kan flyttes til venstre for celle 0, men det finnes nok andre implementasjoner der dette vil gi et annet resultat.

Videoen inneholder også video av hvordan disse tegnene skal tolkes, så forhåpentligvis har det ikke skapt unødvendig forvirring.


## Løsning

Tid brukt: 30 minutter

Denne oppgaven var litt rar. En video med brainfuck kode med streamet. En mann fra Novacare brukte en slags dans for å skrive koden. Dette er koden vi fikk fra videoen:
```brainfuck
++++++++++[>+++++>+++++++>++++++++++>+++++++++++>+++++++++++<<<<<<<-]>>+++++.>>>++++.<+.+..+++.<+++++ ++.>-.<<<--.>>+..
```

Ingen online interpretere ville kjøre koden, så jeg valgte å spør ChatGPT4 om litt hjelp. Etter mye tulling og masing kom han endelig frem til svaret med følgende kode:

```python
def bf_interpreter_safe(code):
    tape = [0] * 30000  # Initialize the tape with 30,000 cells set to 0
    ptr = 0  # Set the pointer to the start of the tape
    i = 0  # Instruction pointer
    output = ""  # Initialize output string
    loop_stack = []  # Stack to hold the loop starting positions

    while i < len(code):
        cmd = code[i]
        if cmd == '>':
            ptr = min(ptr + 1, len(tape) - 1)  # Prevent the pointer from exceeding the right end of the tape
        elif cmd == '<':
            ptr = max(ptr - 1, 0)  # Prevent the pointer from going before the start of the tape
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256  # Ensure the cell value wraps around 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256  # Ensure the cell value wraps around 256
        elif cmd == '.':
            output += chr(tape[ptr])
        elif cmd == '[':
            if tape[ptr] == 0:  # If the current cell is 0, jump past the matching ']'
                open_loops = 1
                while open_loops > 0:
                    i += 1
                    if code[i] == '[':
                        open_loops += 1
                    elif code[i] == ']':
                        open_loops -= 1
            else:
                loop_stack.append(i)
        elif cmd == ']':
            if tape[ptr] != 0:  # If the current cell is not 0, jump back to the matching '['
                i = loop_stack[-1]
            else:
                loop_stack.pop()
        i += 1  # Move to the next instruction

    return output

# Re-run the interpreter with the adjusted version
bf_interpreter_safe(code)
```

Kodeord: Kroppskr0ll
