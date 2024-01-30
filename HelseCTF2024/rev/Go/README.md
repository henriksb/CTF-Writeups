### StateOfGo

Mitt Go-program kompilerer fint, men viser ikke flagget? Jeg som trodde Go aldri kunne gjøre noe feil!? Se om det hjelper å overskrive en byte på vilkårlig offset.

#### Løsning
Her får man kildekoden ved å koble til serveren som kjører koden.
```go
package main

import (
	"fmt"
	"os"
)

type N struct {
	data string
	i    int
}

func (n N) get() string {
	return string(n.data[n.i])
}

func main() {
	flag, _ := os.ReadFile("flag.txt")
	n := N{string(flag), -1}
	t := func(n N) N {
		n.i += 1
		return n
	}
	for i := 0; i < len(n.data) i++ {
		n := t(n)
		fmt.Print(n.get())
	}
	fmt.Println()
}
```
Her kan man se at den løkken som gir igjennom bokstavene har en print-funksjon som printer `fmt.Print(n.get())`. Problemet her er at når man kjører denne koden vil man bare få tilbake en bokstav, som er den første bokstaven i flagget. Grunnen til dette er at `n` blir reinitialisert for hver iterasjon av for-løkken. For å fikse dette må man fjerne en kolon fra lihketstegnet. Man må altså gjøre `n := t(n)` til `n = t(n)`. For å gjøre dette bruker man offset 299 for å velge kolon, og så bruker man erstatningstegnet 20 (mellomrom).

Da får man flagget `helsectf{redeclaring_a_Go_variable_can_shadow_another!}`
