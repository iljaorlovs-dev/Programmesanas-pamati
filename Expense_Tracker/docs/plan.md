#Programmas apraksts
Programma ļauj pierakstīt izmaksas lietojot CLI, kā arī pārvaldīt tos pierakstus. Viņa saglābā  izmaksu statistiku pa mēnešiem un kategorijām un ļauj eksportēt datus.


#Datu struktūra
Plānotā datus struktūra - vienkāršākā ar tikai vajadzīgiem datiem, kuri ļauj strukturēt datus, dzēst pierakstus, sortēt:
    "date": "2025-02-15",
    "amount": 12.50,
    "category": "Ēdiens",
    "description": "Pusdienas"

#Moduļu plāns
├── app.py        # Galvenā programma (izvēlne, lietotāja mijiedarbība) 
├── storage.py    # JSON failu operācijas 
├── logic.py      # Biznesa loģika (filtrēšana, grupēšana, summas) 
├── export.py     # CSV eksports 
└── expenses.json # Dati (izveidojas automātiski) 


#Funkciju piemēri
storage.py
    load_expenses()
    save_expenses()

logic.py
    filter_by_month()
    sum_total()
    sum_by_category()

export.py
    export_to_csv()

app.py
    show_menu()
    add_expense()
    delete_expense()



#Lietošanas scenāriji
Kad tiek ievādītas izmaksas, programma tos saglābā json failā.
Programma apstiprina, ka izmaksas ir saglābatas.
Ja tiek ievādīts nepareizais formāts, programma nepārtāj strādāt un rāda attiecīgu formāta kļūdu. Katrā rindā būtu labi paradīt gaidāmo datu formātu (piem lai nesajauktu , un . ciparos). Jāparedz visādas kļūdas- negatīvas vertības, drukas kļūdas, tukšas vertības.
Json fails veidojas automātiski un ja tur nav datu, programma rāda, ka dati ir tukši.
