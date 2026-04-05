from storage import load_expenses, save_expenses
from logic import sum_total

# Predefined categories
CATEGORIES = [
    "Ēdiens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits",
]


def show_menu():
    """Display menu and return user choice."""
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("7) Iziet")
    return input("\nIzvēlies: ")


def add_expense(expenses):
    """Add a new expense with validation and retry."""

    # --- DATE ---
    while True:
        date = input("Datums (YYYY-MM-DD): ").strip()

        if date == "":
            print("Datums nevar būt tukšs!")
            continue

        # (простая проверка, полноценную добавим позже)
        if len(date) != 10 or date[4] != "-" or date[7] != "-":
            print("Nepareizs datuma formāts! (YYYY-MM-DD)")
            continue

        break

    # --- CATEGORY ---
    while True:
        print("\nKategorija:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"{i}) {cat}")

        choice = input("Izvēlies kategoriju: ").strip()

        if not choice.isdigit():
            print("Ievadi skaitli!")
            continue

        index = int(choice) - 1

        if 0 <= index < len(CATEGORIES):
            category = CATEGORIES[index]
            break
        else:
            print("Nepareiza izvēle!")

    # --- AMOUNT ---
    while True:
        amount_input = input("Summa (EUR): ").strip()

        if amount_input == "":
            print("Summa nevar būt tukša!")
            continue

        # normalize comma → dot
        amount_input = amount_input.replace(",", ".")

        try:
            amount = float(amount_input)

            if amount <= 0:
                print("Summai jābūt pozitīvai!")
                continue

            break

        except ValueError:
            print("Nepareiza summa!")

    # --- DESCRIPTION ---
    description = input("Apraksts (var būt tukšs): ").strip()

    # --- CREATE RECORD ---
    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description,
    }

    # --- SAVE ---
    expenses.append(expense)
    save_expenses(expenses)

    print(f"\n✓ Pievienots: {date} | {category} | {amount:.2f} EUR | {description}")


def show_expenses(expenses):
    """Display all expenses with total."""

    if not expenses:
        print("Nav datu.")
        return

    print("\nDatums       Summa    Kategorija    Apraksts")
    print("-" * 50)

    for e in expenses:
        print(f"{e['date']}  {e['amount']:.2f}  {e['category']}  {e['description']}")

    print("-" * 50)
    print(f"Kopā: {sum_total(expenses):.2f} EUR")


def main():
    """Main program loop."""

    expenses = load_expenses()

    while True:
        choice = show_menu()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "7":
            print("Uz redzēšanos!")
            break

        else:
            print("Nepareiza izvēle!")


if __name__ == "__main__":
    main()