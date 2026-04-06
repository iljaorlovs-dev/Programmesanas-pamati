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
Izmantoju while ciklus ar atkārtotu ievadi un .get() drošai piekļuvei datiem

## 3. solis: Filtrēšana, kopsavilkums un dzēšana
sum_by_category - tiek pievienota atsevišķa vardnīca TOTALS logic.py
get_available_months() taisa set ar unikālām vērtībām logic.py, bet lietotājam atgriežam datus kā list (lai strādātu sorting).
App.py uzsākta delete_expenses funkcija. Python lieto nulli kā sākumskaitli (bet lietotāj redz 1 kā sākumskatli), removed = expenses.pop(index - 1).
Piemirsu atjaunot menu, tāpēc testēšana no sākuma nebija sekmīga, jo nebija jaunu opciju.
Sarežģītākā daļa bija dzēšanas funkcija - vajadzēja pareizi apstrādāt lietotāja ievadi.
Uzlabota app.py importa funkcija, apvienojot visus ierakstus no logic.py vienā komandā pēc MI ieteikumiem.
Uzlabots storage.py ar json faila lokācijas piesaistīšanu.
Logic.py bija palaisa gada un mēneša validācija, Chat gpt tas bija ok, Claude tas nepatika, pafiksēts.

## 4. solis: CSV exports
Izveidoju export.py moduli ar funkciju eksportam uz CSV.
Pievienota piespiedu .csv fomāta pievienošana.
Pievienota aizsardzība no space nosaukumos.

## 5. README
Garlaicīgākā daļa. Uzrakstīts ar MI.


## 6. PS
Nākotnē plāns pievienot:
- grafisko interfeisu
- datu importu
- lietotāja autentifikāciju

