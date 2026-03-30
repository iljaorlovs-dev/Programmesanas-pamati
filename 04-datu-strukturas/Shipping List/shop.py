import sys
from storage import load_list, save_list, get_price, set_price
from utils import calc_line_total, calc_grand_total, count_units


def add_item(name, qty):
    items = load_list()

    # 🔢 Проверка количества
    try:
        qty = int(qty)
        if qty <= 0:
            print("Quantity must be positive")
            return
    except ValueError:
        print("Invalid quantity")
        return

    # 🔍 ищем цену (делаем name маленьким для стабильности)
    name_key = name.lower()
    price = get_price(name_key)

    if price is not None:
        print(f"Found price: {price:.2f} EUR/unit")

        choice = input("[A]ccept / [M]odify? > ").strip().lower()

        if choice == "m":
            try:
                price = float(input("New price: > "))
                if price <= 0:
                    print("Price must be positive")
                    return
                set_price(name_key, price)
                print(f"✓ Price updated: {name} → {price:.2f} EUR")
            except ValueError:
                print("Invalid price")
                return

    else:
        print("Price not found.")
        try:
            price = float(input("Enter price: > "))
            if price <= 0:
                print("Price must be positive")
                return
            set_price(name_key, price)
            print(f"✓ Price saved: {name} ({price:.2f} EUR)")
        except ValueError:
            print("Invalid price")
            return

    # 🔁 объединение товаров
    for item in items:
        if item["name"].lower() == name_key:
            item["qty"] += qty
            save_list(items)

            line_total = calc_line_total(item)
            print(f"✓ Updated: {name} × {item['qty']} = {line_total:.2f} EUR")
            return

    # ➕ новый товар
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

    if not items:
        print("Shopping list is empty.")
        return

    total_price = calc_grand_total(items)
    total_units = count_units(items)

    print(f"Total: {total_price:.2f} EUR "
          f"({total_units} units, {len(items)} products)")


def clear():
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
        if len(args) != 4:
            print("Usage: add <name> <qty>")
        else:
            add_item(args[2], args[3])

    elif command == "list":
        show_list()

    elif command == "total":
        total()

    elif command == "clear":
        clear()

    else:
        print("Unknown command")