from storage import load_expenses, save_expenses
from logic import sum_total, is_valid_date
from datetime import date
from logic import get_available_months, filter_by_month

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
    print("3) Filtrēt pēc mēneša")
    print("5) Dzēst izdevumu")
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
        exp_date = e.get("date", "")
        amount = e.get("amount", 0)
        category = e.get("category", "")
        description = e.get("description", "")
        if len(description) > 20:
            description = description[:17] + "..."

        # Format output with fixed width columns
        print(f"{i:<2} {exp_date:<12} {amount:>8.2f}   {category:<20} {description}")

    print("-" * 65)

    # Total
    total = sum_total(expenses)
    print(f"Kopā: {total:.2f} EUR ({len(expenses)} ieraksti)")


def delete_expense(expenses):
    """Delete an expense by its number."""

    if not expenses:
        print("Nav datu.")
        return

    print("\nIzdevumi:")

    for i, e in enumerate(expenses, 1):
        print(f"{i}) {e['date']} | {e['amount']:.2f} EUR | {e['category']} | {e['description']}")

    while True:
        choice = input("\nKuru dzēst? (numurs vai 0 lai atceltu): ").strip()

        if not choice.isdigit():
            print("Ievadi skaitli!")
            continue

        index = int(choice)

        if index == 0:
            print("Dzēšana atcelta.")
            return

        if 1 <= index <= len(expenses):
            removed = expenses.pop(index - 1)
            save_expenses(expenses)

            print(f"\n✓ Dzēsts: {removed['date']} | {removed['amount']:.2f} EUR | {removed['category']} | {removed['description']}")
            return
        else:
            print("Nepareizs numurs!")


def filter_expenses_by_month(expenses):
    """Filter and display expenses by selected month."""

    months = get_available_months(expenses)

    if not months:
        print("Nav datu.")
        return

    print("\nPieejamie mēneši:")
    for i, m in enumerate(months, 1):
        print(f"{i}) {m}")

    while True:
        choice = input("Izvēlies mēnesi: ").strip()

        if not choice.isdigit():
            print("Ievadi skaitli!")
            continue

        index = int(choice) - 1

        if 0 <= index < len(months):
            selected = months[index]
            break
        else:
            print("Nepareiza izvēle!")

    # Split year and month
    year_str, month_str = selected.split("-")
    year = int(year_str)
    month = int(month_str)

    # Filter data
    filtered = filter_by_month(expenses, year, month)

    print(f"\n{selected} izdevumi:")

    if not filtered:
        print("Nav datu.")
        return

    for e in filtered:
        print(f"{e['date']} | {e['amount']:.2f} EUR | {e['category']} | {e['description']}")

    print(f"\nKopā: {sum_total(filtered):.2f} EUR ({len(filtered)} ieraksti)")




def main():
    """Main program loop."""

    expenses = load_expenses()

    while True:
        choice = show_menu()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            filter_expenses_by_month(expenses)

        elif choice == "5":
            delete_expense(expenses)    

        elif choice == "7":
            print("Uz redzēšanos!")
            break

        else:
            print("Nepareiza izvēle!")


if __name__ == "__main__":
    main()
