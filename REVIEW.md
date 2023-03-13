Reviewpartner: Fien Visser

## Verbeterpunten
- Util.py heeft een link naar een afbeelding: ik zou adviseren om de afbeelding lokaal op te slaan ipv de link toe te voegen. Zo weet je zeker dat je altijd toegang hebt tot deze foto en er geen problemen ontstaan. Daarnaast ziet dat er netter uit dan een hele link.
- Ik zou in views.py nog wat comments aanmaakt om te laten zien waar elke functie voor is.
- Binnen searchres functie heb je een if statement, maar niet een else voor als je niet aan die conditie voldoet. Bijvoorbeeld als je op de eerste pagina niet iets invult in de search bar en wel op zoeken klikt, krijg je nu een soort aanbeveling. Ik zou zelf adviseren om een error pagina aan te maken zodat je alle mogelijke scenarios hebt ingedekt, met if en else.
- De verschillende variabelen die je aanmaakt binnen je functies in views.py zijn wat verwarrend voor mij. Ik had misschien iets duidelijkere termen gebruikt zodat je het overzicht niet verliest.
- Je zou nog even dingen kunnen verwijderen die je niet gebruikt, zoals als er in css een class is zonder style attributes. Of zoals dat je in views.py iets importeerd (markdown) wat je niet gebruikt.

## Vragen
- Waarom link van naar een afbeelding online, en geen lokale afbeelding binnen de projectmap?
- Waarom geen errorpagina bij geen invoer in de zoekmachine?
- Waarom zoveel verschillende namen voor variabelen in views.py?
- Soms wordt er niks meegeven aan functies in views.py om een pagina te generen, is dit okay?
- Is de indeling van de templates in de mappen juist? Kunnen ze ook bestaan zonder een 'extra' 'search' map?

## Uitwerking Review
Bij het eerste punt is het probleem dat ik een afbeelding, die online staat, heb genomen om te dienen als icon, in plaats van er een op te slaan in een van mijn mappen, om deze te gebruiken. Hierdoor kan het zo zijn dat de afbeeldingpagina op wikipedia wordt gewijzigd en daardoor mijn icon ook. Het probleem is dus dat ik een bepaalde factor uit handen geef, en deze niet kan controleren. Het kan beter door de icon in een van mijn eigen mappen op te slaan, zodt deze altijd beschikbaar is. Ik zou dit bijvoorbeeld bij de icon kunnen doen, en bij de hoofdbalk met de paginaknoppen, die een achtergrond heeft van een schilderij dat online staat. Tot slot zou dit de link, en dus de code, iets korter maken.

Bij het tweede punt gaat het om de comments die ik nog had kunnen toevoegen om enige duidelijkheid te bieden over wat de code op welk punt doet. Als ik deze zou toevoegen is het gemakkelijker om de code te volgen. Voorbeelden van waar dit zou kunnen, zijn de searchres and adsearchres functies.

Het derde punt gaat vooral over het afvangen van een zogeheten corner case, en het schrijven van code hiervoor. Dit ontbreekt voor het geval dat een gebruiker niks invult in de zoekbalk, maar wel op 'enter' drukt. Hierbij worden door mijn zoekmachine wel resultaten gegeven, die vanuit de Rijks API komen. Dit zou echter niet perse het resultaat moeten zijn. Voor de hand liggender zou een pagina zijn die aangeeft dat er een error is, aangezien er geen zoekterm is ingevuld. Dit zou kunnen worden verholpen door een if die deze case af kan vangen. Zo krijgt men bijvoorbeeld een pagina die de gebruiker wijst op het feit dat er een zoekterm nodig is.  

Bij het vierde punt gaat het vooral om het hebben van duidelijke variabelen. Ik maak in de views.py meerdere variabelen aan waar ik ook slimmer had kunnen zijn in het hergebruiken van variabelen. Hierdoor wordt het iets wat onoverzichtelijk, en komt dit niet ten goede aan de code kwaliteit. Ik had beter beter de variabelen kunnen hergebruiken en om de goede momenten een nieuwe waarde hieraan kunnen toeschrijven, zodat ik alleen de minimaal nodige variabelen gebruik. Voorbeelden zijn de variabelen die ik gebruik voor het ophalen, converteren en parsen van de data vanuit de request aan de Cleveland Art Museum API.

Bij het vijfde punt gaat het om het weghalen van zaken die ik niet gebruik in mijn code. Er zijn een aantal zaken die ik niet (meer) gebruik, en welke ik voor de overzichtelijkheid van de code kan weghalen. Een voorbeeld is een class die in mijn css style sheet leeg is, en een aantal zaken die ik heb geimporteerd, maat niet heb gebruikt, zoals markdown in views.py.

Verder zijn er wat betreft de vragen nog twee punten. Sommige functies renderen inderdaad een pagina zonder iets mee te geven. Dit komt omdat ze altijd alleen wat tekst zullen weergeven. Hiernaats zijn de 'extra' mappen gemaakt naar het voorbeeld van het Django college. Ik heb dit als blauwdruk genomen voor mijn indeling.

Tot slot zijn er nog een aantal zaken die ik graag had willen verbeteren, maar waarvoor ik geen tijd heb gehad. Voorbeelden zijn de in het procesboek beschreven functionaliteiten van de Advanced search query voor het Cleveland Art Museum, het beter filteren van de zoekresultaten in de normale search - zodat er geen schijnbaar ongerelateerde resultaten worden getoond, en het linken naar de orginele Rijksmuseum- en Cleveland Art Museumpagina.
