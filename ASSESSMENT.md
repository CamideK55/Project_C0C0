# Assessment

## Niet missen : )
- Het gebruik van twee API's - waar de informatie van wordt meegegeven in een lijst met twee dictionaries (een per API) aan de (geavanceerde) zoekresultatenpagina. Deze bestaat elk uit het zippen van twee lijsten, naar een dictionary, die uit de functies komen die de JSON-data filteren.
- Het ontleden van de gewenste informatie uit de JSON files, teruggezonden door het Rijksmuseum en het Cleveland Museum of Art.
- Het feit dat twee verschillende museumcollecties tegelijkertijd inzichtelijk worden gemaakt.

## Grote beslissingen

- Met API: de API van het Metropolitan Museum of Art was de oorspronkelijke API die ik op het oog had om te implementern naast die van het Rijksmuseum. Ik heb uiteindelijk besloten om af te zien van deze implementatie. De reden hiervoor is dat de API zo functioneerde dat men eerst alleen de objectnummers terugkreeg van een request. Met deze resultaten moest een volged request worden gestuurd om de daadwerkelijke informatie te bemachtigen. Dit laatste zorgde voor veel errors en een lange wachttijd voor de resultaten. Verder bestond er geen workaround om dit probleem direct op te lossen. Hierdoor moest ik op zoek naar een alternatief. De les die ik hieruit trek om is om de API goed te bestuderen alsvorens ik hem selecteer om te implementern. De alternatieve API heeft hier uiteindelijk de oplossing geboden.

- Advanced Search Cleveland API: de alternatieve oplossing was uiteindelijk een andere API welke zich meer gedroeg naar mijn vereisten. Hierdoor heb ik de beslissing genomen om deze te implementeren. Deze oplossing werkt een stuk beter, daar het het resultaat biedt waar ik op zoek naar was, maar brengt op zijn beurt ook weer wat problemen met zich mee. Dit gaat vooral om het implementeren van de parameters voor de search. Deze heb ik moeten beperken aangezien ik ze niet alle werkende kon krijgen. Hierdoor is er een oplossing, maar is deze niet zo optimaal als ik had gehoopt.
