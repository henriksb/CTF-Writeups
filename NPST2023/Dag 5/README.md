# Muldvarpjakt

## Oppgavetekst
Gjennom temmelig hemmelige innhentingsmetoder har vi fanget opp en melding om et nært forestående møte på Fastlands-Norge mellom en mistenkt kildefører som jobber for sydpolare tjenester og et ukjent objekt vi mistenker kan være en muldvarp.

For at våre spaningsalver skal settes i stand til å observere møtet og identifisere det ukjente objektet må vi vite hvor vi skal sende våre alver.

Vi prøvde å spørre OSINT-alvene våre, men de var travelt opptatt med å saumfare sosiale medier etter snille og slemme barn. De mumlet noe om at vi kunne fikse det selv med “turbo overgang”.

Kan du ut fra meldingen finne ut hvor de skal møtes?

```
Ta bussen og gå av på holdeplassen rett ved begravelsesbyrået som ligger inntil en sjømatbutikk. Jeg vil stå klar
ved fontenen noen titalls meter fra bussholdeplassen. Når du har kommet frem til fontenen, vil vi sammen gå til
det nærliggende biblioteket som ligger under 50 meter fra fontenen og gjennomfører overføringen.
```

Svar meg med navnet på møtestedet og på formen PST{BERGEN LUFTHAVN}

- Tastefinger

## Løsning

Brukte https://overpass-turbo.eu/ for første gang med det følgende skriptet:

```
[out:json];
{{geocodeArea:Norway}}->.no;
(
  // Finn sjømatbutikker
  node(area.no)["shop"="seafood"];
  way(area.no)["shop"="seafood"];
  relation(area.no)["shop"="seafood"];
  
  node(area.no)["amenity"="fountain"];
  way(area.no)["amenity"="fountain"];
  relation(area.no)["amenity"="fountain"];
  
  node(area.no)["amenity"="library"];
  way(area.no)["amenity"="library"];
  relation(area.no)["amenity"="library"];
  
  // Finn bibliotek
  //node(area.no)["amenity"="funeral_hall"](around.sfood:50);
  //way(area.no)["amenity"="funeral_hall"];
  //relation(area.no)["amenity"="funeral_hall"];
  
);
out center;

{{style:
  node[amenity=fountain],
  way[amenity=fountain],
  relation[amenity=fountain]
{ color:blue; fill-color:blue; }

  node[amenity=library],
  way[amenity=library],
  relation[amenity=library]
{ color:blue; fill-color:green; }

  node[shop=seafood],
  way[shop=seafood],
  relation[shop=seafood]
{ color:blue; fill-color:red; }
}}
```

Jeg endret fargen på de ulike fasilitetene og letet etter en rød, blå og grønn prikk som var nærme på kartet.

Svar: PST{Frogn Bibliotek}
