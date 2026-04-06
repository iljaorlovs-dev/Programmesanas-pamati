#Programmas apraksts
Programma ir CLI rīks, kas ļauj lietotājam reģistrēt ikdienas izdevumus, analizēt tos pa mēnešiem un kategorijām, kā arī eksportēt datus CSV formātā.


#Datu struktūra
Plānotā datus struktūra - vienkāršākā ar tikai vajadzīgiem datiem, kuri ļauj strukturēt datus, dzēst pierakstus, sortēt. Dati tiek glabāti kā saraksts (list), kur katrs elements ir vārdnīca (dict). Tas ļauj viegli pievienot jaunus ierakstus, saglabāt secību un dzēst ierakstus pēc indeksa.
Vārdnīca ļauj katram ierakstam strukturēti glabāt laukus (datums, summa, kategorija, apraksts).
    "date": "2025-02-15",
    "amount": 12.50,
    "category": "Ēdiens",
    "description": "Pusdienas"

#Moduļu plāns
├── app.py        # Galvenā programma (izvēlne, lietotāja mijiedarbība) - neaprēķina summas
├── storage.py    # JSON failu operācijas - nesatur print/input
├── logic.py      # Biznesa loģika (filtrēšana, grupēšana, summas) - nestrādā ar failiem
├── export.py     # CSV eksports 
└── expenses.json # Dati (izveidojas automātiski) 


#Funkciju piemēri
storage.py
    load_expenses() #nolasa datus no JSON faila
    save_expenses() #saglabā datus JSON failā

logic.py
    filter_by_month() #atgriež izdevumus konkrētam mēnesim
    sum_total() #aprēķina kopējo summu
    sum_by_category() #summēšana pa izmaksu kategorijām

export.py
    export_to_csv() #eksports csv failā

app.py
    show_menu() #programmas izvēlne
    add_expense() #izmaksu pievienošana
    delete_expense() #izmaksu dzešana



#Lietošanas scenāriji
Kad tiek ievādītas izmaksas, programma tos saglābā json failā.
Programma apstiprina, ka izmaksas ir saglābatas.
Ja tiek ievādīts nepareizais formāts, programma nepārstāj strādāt un rāda attiecīgu formāta kļūdu (piemēram, lietotājs ievada nepareizu datumu (piem. 2025/02/15).
Programma parāda kļūdu un lūdz ievadīt vēlreiz.). Katrā rindā būtu labi paradīt gaidāmo datu formātu (piem lai nesajauktu , un . ciparos). Jāparedz visādas kļūdas- negatīvas vertības (Lietotājs pievieno izdevumu ar negatīvu summu -> programma nepieņem ievadi un parāda kļūdu), drukas kļūdas, tukšas vertības.
Json fails veidojas automātiski un ja tur nav datu, programma rāda, ka dati ir tukši (ja lietotājs izvēlas “Parādīt izdevumus”, bet saraksts ir tukšs. Programma parāda ziņu: “Nav datu”).



#Algoritmu piemēri
    1. Programma prasa ievadīt datumu (YYYY-MM-DD)

    2. Ja datums ir tukšs vai nepareizā formātā
    → parāda kļūdu un prasa ievadīt vēlreiz

    3. Programma prasa ievadīt summu

    4. Aizvieto "," ar "." (normalizācija)

    5. Ja summa nav skaitlis vai <= 0
    → parāda kļūdu un prasa ievadīt vēlreiz

    6. Programma parāda kategoriju sarakstu

    7. Lietotājs izvēlas kategoriju
    Ja izvēle nav derīga
    → piedāvā ievadīt jaunu kategoriju -tas tiks īstenos nākāmajās versijās :-)

    8. Programma prasa aprakstu (var būt tukšs)

    9. Izveido ierakstu (dict)

    10. Pievieno ierakstu sarakstam

    11. Saglabā JSON failā

    12. Parāda apstiprinājumu