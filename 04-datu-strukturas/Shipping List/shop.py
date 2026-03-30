import sys
from storage import load_list, save_list
from utils import calc_line_total, calc_grand_total, count_units


def add_item(name, qty, price):
    items = load_list()

    try:
        qty = int(qty)
        price = float(price)

        if qty <= 0:
            print("Quantity must be positive")
            return

    except ValueError:
        print("Invalid number")
        return

    item = {
        "name": name,
        "qty": qty,
        "price": price
    }

    items.append(item)
    save_list(items)

    line_total = calc_line_total(item)

    print(f"✓ Added: {name} × {qty} ({price:.2f} EUR/unit) = {line_total:.2f} EUR")


def show_list():
    items = load_list()

    if not items:
        print("Shopping list is empty.")
        return

    print("Shopping list:")

    for i, item in enumerate(items, start=1):
        line_total = calc_line_total(item)

        print(f"  {i}. {item['name']} × {item['qty']} — "
              f"{item['price']:.2f} EUR/unit — {line_total:.2f} EUR")


def total():
    items = load_list()

    total_price = calc_grand_total(items)
    total_units = count_units(items)

    print(f"Total: {total_price:.2f} EUR "
          f"({total_units} units, {len(items)} products)")
    


def clear():
    """
    Очищает список.
    """
    save_list([])
    print("✓ List cleared")


# ===== CLI обработка =====
if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        print("Usage: add/list/total/clear")
        sys.exit()

    command = args[1]

    if command == "add":
    if len(args) != 5:
        print("Usage: add <name> <qty> <price>")
    else:
        add_item(args[2], args[3], args[4])

    elif command == "list":
        show_list()

    elif command == "total":
        total()

    elif command == "clear":
        clear()

    else:
        print("Unknown command")