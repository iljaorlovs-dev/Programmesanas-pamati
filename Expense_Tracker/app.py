from storage import load_expenses, save_expenses
from logic import sum_total, is_valid_date
from datetime import date

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
    today = date.today().strftime("%Y-%m-%d")

    while True:
        date_input = input(f"Datums (YYYY-MM-DD) [{today}]: ").strip()

        if date_input == "":
            date_input = today

        if is_valid_date(date_input):
            expense_date = date_input
            break
        else:
            print("Nepareizs datums! Izmanto formātu YYYY-MM-DD.")
            continue

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
        "date": expense_date,
        "amount": amount,
        "category": category,
        "description": description,
    }

    # --- SAVE ---
    expenses.append(expense)
    save_expenses(expenses)

    print(f"\n✓ Pievienots: {expense_date} | {category} | {amount:.2f} EUR | {description}")


def show_expenses(expenses):
    """Display all expenses in a formatted table with numbering."""

    if not expenses:
        print("Nav datu.")
        return

    # Table header
    print("\n#  Datums       Summa     Kategorija           Apraksts")
    print("-" * 65)

    # Loop through expenses with numbering
    for i, e in enumerate(expenses, 1):
        date = e.get("date", "")
        amount = e.get("amount", 0)
        category = e.get("category", "")
        description = e.get("description", "")

        # Format output with fixed width columns
        print(f"{i:<2} {date:<12} {amount:>8.2f}   {category:<20} {description}")

    print("-" * 65)

    # Total
    total = sum_total(expenses)
    print(f"Kopā: {total:.2f} EUR ({len(expenses)} ieraksti)")


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