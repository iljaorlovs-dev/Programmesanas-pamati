# Expense Tracker (CLI) ver ORL 0.1

## 📌 Project Description

Expense Tracker is a command-line (CLI) application written in Python that allows users to track their daily expenses.

The program supports adding, viewing, filtering, deleting expenses and exporting data to CSV format. All data is stored in a JSON file and persists between program runs.

---

## 🚀 Features

* Add new expenses (date, amount, category, description)
* View all expenses in a formatted table
* Filter expenses by month
* View summary by category
* Delete expenses by number
* Export data to CSV (Excel-compatible)
* Data persistence using JSON

---

## 🛠 Technologies Used

* Python 3
* Built-in modules:

  * `json`
  * `datetime`
  * `csv`

---

## 📂 Project Structure

```
expense_tracker/
│
├── app.py        # Main program (CLI interface)
├── storage.py    # JSON file operations
├── logic.py      # Business logic (filtering, calculations)
├── export.py     # CSV export
├── expenses.json # Data file (auto-created)
│
docs/
├── plan.md
├── DEVLOG.md
```

---

## ▶️ How to Run

1. Clone the repository or download the files
2. Open terminal in project folder
3. Run:

```
python app.py
```

---

## 💡 Example Usage

```
1) Pievienot izdevumu
2) Parādīt izdevumus
3) Filtrēt pēc mēneša
4) Kopsavilkums pa kategorijām
5) Dzēst izdevumu
6) Eksportēt CSV
7) Iziet
```

---

## 📊 Data Format (JSON)

```
[
  {
    "date": "2025-02-15",
    "amount": 12.50,
    "category": "Ēdiens",
    "description": "Pusdienas"
  }
]
```

---

## 📤 CSV Export

The program supports exporting data to CSV format using UTF-8 encoding (`utf-8-sig`) to ensure compatibility with Excel and proper display of Latvian characters.

---

## 🧠 Key Concepts

* Modular architecture (separation of concerns)
* Input validation and error handling
* Data persistence (JSON)
* Data processing (filtering, grouping)
* CLI user interaction

---

## 📌 Author

Ilja Orlovs + Chat GPT + Claude review
