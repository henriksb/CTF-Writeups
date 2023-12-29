# Bokorm

## Oppgavetekst
En snok vi mistenker å stå i ledetog med Pen GWYN har blitt arrestert etter å ha brutt seg inn i NordPolarBiblioteket og stjålet noen bøker. Vi mistenker at de har vært ute etter noe spesifikt, men vi blir ikke helt kloke på hva det er. Snoken ble tatt med en stabel bøker og et notat.

Bøkene har vi gitt tilbake til biblioteket, men her er en liste av dem som ble stjålet:
```
Norrøn arverett og samfunnsstruktur
Radium og radioaktive stoffer, samt nyere opdagelser angaaende straaler
Undertrykking av objekter med høy luminans ved hjelp av en romlig lysmodulator under avbildning med CCD- og lysforsterkningskamera
Om den yngre Jernalder i Norge : 1. afdeling
Storlogens Konstitution og Tillægslove
Sild- og saltfiskretter
```

Notatet inneholdt dette her:
```
(55, 1, 2, 1), (65, 17, 6, 3), (19, 3, 8, 1), (13, 5, 6, 2), (14, 11, 4, 8), (27, 32, 12, 2), (9, 7, 12, 3), (82, 5, 2, 8), (78, 3, 11, 1), (71, 5, 1, 8), (76, 1, 6, 2), (92, 1, 1, 1), (50, 2, 1, 5), (15, 1, 1, 1), (82, 16, 10, 4), (23, 6, 1, 1), (34, 16, 7, 1), (92, 11, 3, 2), (50, 5, 6, 1), (1, 3, 5, 12), (42, 2, 1, 1), (15, 3, 1, 3), (23, 8, 1, 2), (90, 2, 5, 1), (83, 1, 1, 2), (59, 29, 9, 4), (93, 4, 1, 16), (82, 8, 3, 5), (39, 1, 1, 8), (77, 7, 9, 1), (93, 8, 6, 8), (1, 1, 3, 6), (83, 10, 8, 1), (23, 1, 1, 1), (69, 2, 9, 2), (76, 12, 3, 4), (7, 1, 3, 1), (3, 9, 9, 2), (19, 1, 6, 10), (93, 14, 7, 5), (13, 31, 7, 10), (3, 1, 9, 2), (7, 2, 6, 1), (23, 19, 4, 3), (50, 6, 5, 11)
```

Send svar til meg om du finner ut av det.

- Tastefinger

## Løsning
```
(55, 1, 2, 1),   l, p, k, p, X, X
(65, 17, 6, 3),  t, a, r, s, X, X
(19, 3, 8, 1),   f, s, t, t, X, s
(13, 5, 6, 2),   ø, r, X, k, a, g
(14, 11, 4, 8),  X, X, X, r, s, e
(27, 32, 12, 2), i, X, X, s, X, X
(9, 7, 12, 3),   n, X, D, l, X, X
(82, 5, 2, 8),   X, X, X, l, X, X
(78, 3, 11, 1),  b, X, a, P, X, X
(71, 5, 1, 8),   a, X, X, a, X, X 
(76, 1, 6, 2),   e, n, i, r, X, X
(92, 1, 1, 1),   m, m, n, e, X, X
(50, 2, 1, 5),   e, X, t, n, X, X 
(15, 1, 1, 1),   f, i, X, T, A, K
(82, 16, 10, 4), X, X, t, l, X, X
(23, 6, 1, 1),   t, F, l, S, V, L
(34, 16, 7, 1),  s, X, a, b, 
(92, 11, 3, 2),  X, X, X, o
(50, 5, 6, 1),   X, X, X, K
(1, 3, 5, 12),   X, X, X, s
(42, 2, 1, 1),   X, X, X, t
(15, 3, 1, 3),   X, X, X, a
(23, 8, 1, 2),   X, X, X, v
(90, 2, 5, 1),   X, X, X, j
(83, 1, 1, 2),   X, X, X, a
(59, 29, 9, 4),  X, X, X, k
(93, 4, 1, 16),  X, X, X, t
(82, 8, 3, 5),   X, X, X, k
(39, 1, 1, 8), 
(77, 7, 9, 1), 
(93, 8, 6, 8), 
(1, 1, 3, 6), 
(83, 10, 8, 1), 
(23, 1, 1, 1), 
(69, 2, 9, 2), 
(76, 12, 3, 4), 
(7, 1, 3, 1), 
(3, 9, 9, 2), 
(19, 1, 6, 10), 
(93, 14, 7, 5), 
(13, 31, 7, 10), 
(3, 1, 9, 2), 
(7, 2, 6, 1), 
(23, 19, 4, 3), 
(50, 6, 5, 11)
```

Googlet "book cipher" og fant formatet "page - line - word - letter", som matchet settene med fire tall.
https://www.dcode.fr/book-cipher

For å få tak i bøkene brukte jeg https://www.nb.no/, hvor man kan låne alle bøkene man trenger.

Som du kan se ovenfor, begynte jeg å manuelt finne alle bokstavene som matchet tallene. Da jeg kom til linje 16 merket jeg at bok 4 (Om den yngre Jernalder i Norge : 1. Afdeling) inneholdt noe som lignet på "PSTKRØLLPARENTES". Jeg fortsatte da å kun bygge på den frem til "bokstavjakt" var funnet. Da antok jeg at de siste tallene var "krøllparentes" og leverte inn svaret.

Svar: PST{bokstavjakt}
