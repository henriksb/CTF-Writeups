# Bit-råte

## Filer
📎backups.zip

## Oppgavetekst
Brukerveiledningen til en av de eldste maskinene på verkstedet har blitt borte. Heldigvis har Julenissens arkiv 1000 sikkerhetskopier av dokumentet på magnetbånd. Det viser seg at alle kopiene er kraftig angrepet av bit-råte så dokumentet må gjenoppbygges. Ifølge arkivalven så er brukerveiledningen skrevet på gammel-nordpolarsk som har samme alfabet som norsk, men inneholder ikke nye tegn som disse: ```{}#$[]§¤@```

Når du finer ut av det så send meg MD5-sjekksummen til det gjenoppbyggede dokumentet på formen PST{checksum}. Svaret er ikke versalfølsomt.

- Mellomleder

## Løsning
Alle 1000 filer inneholder ett dokument, men alle kopiene er angrepet av bit-råte. Vi fjerner først bokstaver som ikke finnes i det gammel-nordpolarske språket ```{}#$[]§¤@```. Deretter finner vi tegn som gjentar seg på alle posisjoner i backupene (hvis første bokstav i backupene er "N" 100 ganger og "B" 50 ganger, så velger vi "N" som førstebokstav). Vi gjør dette for hele lengden av backupene og legger i sammen bokstaver som gjentar seg mest. Til slutt legger alle tegnene i sammen og får dokumentet.

Skriptet produserer følgende tekst:
```
Nordpolen Leketo Skapar Maskin Notendahandbok
Innihald

    Inngangur
    Øryggidiltakan
    Maskínuskyring
    Adalnotkun
    Vidhald og Vandrædaleysingar

1. Inngangur

Velkominn a verkstædi Olafs å Nordurpolinu! Dessi notendahandbok leidir dig i gegnum notkun å vårri gagnryni leikja-skapar maskinar. Dessi maskin er hønnud til ad hjålpa Olafi og hans alfum ad skapa leiki sem skulu færa gledi til barna um allan heim. Lesid dessa handbok varsamlega til ad tryggja ørugga og hagkvæma notkun.
2. Øryggisreglur

Øryggi ditt er okkar helsta markmid å verkstædi Olafs. Vinsamlegast fylgdu eftir eftirfarandi øryggisreglum:

    Ekki snertu hreyfanlegar hluta: Halda hendurnar og føtun dinar i burtu frå hreyfanlegum dåttum maskinunnar til ad koma i veg fyrir slikarhåttar åverkanir.
    Eftirlit: Adeins djålfud ålfar hafa heimild til ad vinna vid maskinuna.
    Nota videigandi flikur: Ålfar ættu ad nota vidbuna vørnartæki, dar å medal gleraugu og vettlinga.
    Neysluønn: Kynntu der stadsetningu neysluønnar og hvernig henni er styrt.

3. Maskinuskyring

Leikja-skapar maskinan å verkstædi Olafs er flokin tæki. Her er yfirlit yfir helstu dåttum hennar:

    Flutningabelti: Flytja hråefni og samsett leiki å milli mismunandi verkfæra.
    Leikjasamsettari: Dar breytast hråefnin i leiki.
    Gædaeftirlitstød: Ålfar skoda leikina eftir galla og gæta dess ad deir uppfylli krøfur Olafs.
    Gjafapakkadarstød: Degar leikirnar hafa farid i gegnum gædaeftirlitid, verda dær pakkadar inn i skrautlegan pappir og undirbunar fyrir afhendingu.

4. Adalnotkun

Fylgdu dessum skrefum til ad nota leikja-skapar maskinina:

Skref 1: Upphaf

    Athugadu ad allar øryggisreglur seu fylgdar.
    Slådu å maskinuna med adalhnappinum.
    Fylgdu med stjorntøflunni eftir møøgulegum villuskilabodum.

Skref 2: Hlada inn hråefnum

    Hlada hråefnum å flutningabeltid.
    Tryggja ad hråefnin seu jøfnlega dreifd til ad få jøfn leikjaaframleidslu.

Skref 3: Samsetning leikja

    Maskinan mun sjålfkrafa byrja samsetningu leikjanna.
    Hlyja samsetningarferlid eftir møøgulegum stoppum eda oregluleikum.
    Nota neysluønnina ef naudsyn ber.

Skref 4: Gædaeftirlit

    Skodadu leikina vid gædaeftirlitsstødina.
    Fjarlægja leiki med galla og setja då i tiltekna kistu.
    Yta å "Samdykkt" hnappinn fyrir leiki sem uppfylla krøfur Olafs.

Skref 5: Gjafapøkkun

    Leikir sem komast fram hjå gædaeftirlitinu verda fluttir å gjafapakkadarstødina.
    Tryggja rett pøkkun og merkingu hvers leiks.
    Setja pakkanadu leikina å serstakt flutningabelt fyrir dreifingu.

Skref 6: Lokun

    Degar vinnan er lokid, sløkkva å maskinunni med adalhnappinum.
    Hreinsa burt ohreinindi frå flutningabeltinu og verkfærunum.

5. Vidhald og Vandrædaleysing

Reglulegt vidhald er naudsynlegt til ad halda leikja-skapar maskinina i bestu åstandi. Skodadu vidhaldsåætlanina sem Olafs Verkstædi bydur upp å.

Vandrædaleysing:

Ef du hittir å vandamål vid maskinuna, skodadu vandamålaleysinguna sem gefin er i serskildri vandamålaleggi sem fylgir.

Takk fyrir ad nota leikja-skapar maskina å Nordurpolinu! Vid vonumst til ad dessi handbok hjålpi der ad nota maskinuna å skilvirkan og øruggan hått.
```

Svar: PST{e32ba07d1254bafd1683b109c0fd6d6c}
