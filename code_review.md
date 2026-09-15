# Kodgranskning av order_report.py

## Utgångsläge
Scriptet körs och skapar 4 olika filer med översikt över köp av varor i olika kategorier och inom regioner. 

## Granskningsfynd

### Fynd 1 - Hela programmet körs på modulnivå vid import

**Observation:** Hela programmet körs på modulnivå. Det finns ingen `main()` så hela rapporten körs vid import.

**Konsekvens:** Import läser och kör hela rapporten, som gör att koden blir svår att testa och återanvända.

**Förslag:** Lägga till en `main()`-funktion som samlar funktioner för programstarten


### Fynd 2 - Fler ansvar är sammanblandade

**Observation:** Läsning, validering, transformation, aggregering, filsparning och status blandas och ligger alla i samma block.

**Konsekvens:** Det bidrar till att olika delar inte kan testas eller återanvändas, allt görs på samma plats.

**Förslag:** Separera delar som hanterar olika områden i egna moduler, exempelvis filhantering och transformationslogik i egna moduler med en pipeline som kopplar ihop.


### Fynd 3 - Logiken är bunden till filflödet

**Observation:** Det går inte att testa beräkningar utan att hela scriptet körs då allt beräknas i try-blocket.

**Konsekvens:** För att kontrollera beräkningsdelar som `order_value` eller `discounted_value` måste hela scriptet köras. Testerna blir därmed långsamma och svårare att se var felen uppstått.

**Förslag:** Skapa en funktion som tar emot en DataFrame och returnerar en ny DataFrame.


### Fynd 4 - Statusmeddelanden använder print()

**Observation:** `print()` används som statusmeddelande genom modulen, att rapporten startas och är klar, att filer sparas och skriver ut felmeddelande.

**Konsekvens:** Format, nivå och destination går inte att styra, och det framgår inte vilken del av programmet som skapade meddelandet. 

**Förslag:** Använd modulloggers för körinformation och konfigurera loggningen centralt vid programmets startpunkt.


### Fynd 5 - Namnen beskriver dataflödet dåligt

**Observation:** Vissa namn som exempelvis `result1` och `result2` säger ingenting om innehållet eller dess roll. Även namnet `data` används på fler ställen trots olika roller. 

**Konsekvens:** Dataflödet blir svårare att följa. Samma namn `data` betyder olika saker på olika rader, vilket gör koden svår att följa uppifrån. 

**Förslag:** Namnge dataframes efter innehåll och roll, samt skilj rådata från bearbetad data.


### Fynd 6 - Sökvägar är hårdkodade

**Observation:** Sökvägen till indatan och namnet på output mappen ligger som konstanter högst upp och de fyra utfilnamnen står direkt i anropen. Scriptet förutsätter dessutom att `output/` redan finns.

**Konsekvens:** Programmet kan inte köras mot en annan fil eller testas tillfälligt utan att koden ändras. 

**Förslag:** Samla sökvägarna i en dataclass med `Path` och låter sparfunktionen skapa målmappen om det behövs.


### Fynd 7 - Grov felhantering

**Observation:** Programmet ligger i ett `try` med ett `except Exception as error` som skriver ut felet med `print()` 

**Konsekvens:** Alla fel behandlas på samma sätt. Det syns inte hur långt körningen hann, som bidrar till att `output` kan bli en blandning av nya och gamla filer. 

**Förslag:** Fånga fel när de uppstår i koden och logga de på ERROR-nivå, exempelvis `FileNotFoundError` vid inläsning och `ValueError` vid validering. 


### Fynd 8 - Aggregering upprepas

**Observation:** Rapporterna: `sales_by_category`, `sales_by_region` och  `returns_by_category` byggs av tre separata kodblock som följer samma mönster: gruppera, aggregera, beräkna return_rate, sortera och spara.  

**Konsekvens:** En ändring i `return_rate` måste göras på tre ställen, som lätt kan glömmas.

**Förslag:** Blocken kan ersättas med en funktion som tar emot grupperingskolumn och mått som ska beräknas och returnerar en färdig dataframe. Rapporterna blir tre anrop.


### Fynd 9 - Datatvätten sker tyst

**Observation:** Saknade och oläsbara värden ersätts automatiskt vid inläsningen och registreras inte någonstans, exempelvis blir text "Unknown" och `quantity` blir 1.

**Konsekvens:** Ett felskrivet pris blir medianpriset och rapporten ser rimlig ut trots fel indata. 

**Förslag:** Räkna de ersatta värdena per kolumn och logga en WARNING när de är fler än noll.


### Fynd 10 - Valideringen ger ett generellt fel

**Observation:** Valideringen kontrollerar att alla nödvändiga kolumner finns, men kastar `Exception("Fel data")` utan att säga vad som saknas.

**Konsekvens:** Felet går inte att felsöka utan att läsa koden. Exception är dessutom för generell för att kunna fångas specifikt i ett test.

**Förslag:** Kasta `ValueError` med namnen på de saknade kolumnerna i meddelandet.