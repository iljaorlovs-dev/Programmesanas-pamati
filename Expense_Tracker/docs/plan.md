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