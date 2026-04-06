# Izstrādes žurnāls 


## 1. solis: Plānošana 
Plan.md veidošanas, struktūras pārdomāšana un aprakstīšana. Izradās, ka aizņem vairāk laika, jo īpaši nesanāk lietot MI kā instrumentu šī posmā.
Tika lemts, ka izmaksu apraksts nav obligāti aizpildāms, komas un punkta lietošana ir atļauta caur datu normalizāciju kā decimālais simbols.


## 2. solis: Pamata darbības
Storage.py logika kā 4. nedēļā
Logic.py - apaļošana notiek galā rezultātā, lai aprēķins būtu matemātiski pareizs. Ar get komandu paredzēta 0 vertība ja datu lauks amount nav aizpildīts.
Datuma validācija noņemta no app.py un ievietota logic.py kā atsevišķa funkcija (jo nav saistīta ar input/output).
Show expenses funkcija optimizēta ar MI palīdzību turpmākām darbībām ar ierakstiem, lai paradītos tabula.
Date nav ieteicams lietot, jo tas konfliktē ar "date" instrumentu, date aizvietots ar expense_date

## 3. solis: Filtrēšana, kopsavilkums un dzēšana
