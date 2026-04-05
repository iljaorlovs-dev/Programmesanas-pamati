#Programmas apraksts
Programma ļauj pierakstīt izmaksas lietojot CLI, kā arī pārvaldīt tos pierakstus. Viņa saglābā  izmaksu statistiku pa mēnešiem un kategorijām un ļauj eksportēt datus.


#Programmas struktūra
├── app.py        # Galvenā programma (izvēlne, lietotāja mijiedarbība) 
├── storage.py    # JSON failu operācijas 
├── logic.py      # Biznesa loģika (filtrēšana, grupēšana, summas) 
├── export.py     # CSV eksports 
└── expenses.json # Dati (izveidojas automātiski) 

#Datu struktūra
Plānotā datus struktūra - vienkāršākā ar tikai vajadīgiem datiem:
    "date": "2025-02-15",
    "amount": 12.50,
    "category": "Ēdiens",
    "description": "Pusdienas"

