## Self reflection

1. Vilka var de viktigaste problemen i originalkoden?

Att hela programmet körs på modulnivå, som leder till att koden blir svår att testa och återanvända. Dessutom att rapportens datatvätt sker tyst, som gör att saknade och oläsbara värden inte registreras någonstans, eftersom de ersätts automatiskt vid inläsningen.

2. Vilka förändringar tycker du förbättrade programmet mest?

Att jag separerade delar som hanterade olika områden i egna moduler, exempelvis filhantering, läsning och validering. Uppdelningen tillsammans med en pipeline bidrar till att möjliggöra återanvändning och tester.

3. Varför valde du den projektstruktur du använde?

Jag valde att strukturera projektet utifrån den ordning datan går igenom med loading till validation till processing till reporting, som kopplas ihop med `__main__`. Det gör det lätt för andra att hitta var varje steg sker.

4. Var använde du OOP/dataclass och varför passade det där?

@dataclass används i `config.py`, specifikt i klassen ReportConfig, som samlar sökvägar och filnamn. Konfigurationen samlar värden men har inget eget beteende och förändras inte under körning. Därför passar dataclass bättre än en vanlig klass, som passar objekt som förändras. Med en dataclass samlas värdena på ett ställe väldigt tydligt.

5. Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?

Mina tester låser fast regler och skyddar då att exempelvis ordervärde räknas rätt samt att felaktig data stoppas. Om någon skulle ändra beräkningarna eller valideringen så fångar testerna upp det och ger ett rött resultat.


6. Vad var svårast?

Det var svårt att hålla sig till att ändra strukturen utan att samtidigt råka ändra resultatet. En svårighet var även att lista ut vad som kan slås ihop och vilka funktioner som skulle få vara kvar separat.

7. Vad hade du velat förbättra ytterligare om du haft mer tid?

Min loop i `prepare_orders` räknar saknade värden innan de omvandlas till tal, så den fångar inte textvärdet i discount. Det hade kunnat lösas genom att räkna saknade värden igen efter `to_numeric`.