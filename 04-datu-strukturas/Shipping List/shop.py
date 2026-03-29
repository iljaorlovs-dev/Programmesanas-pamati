import sys
from storage import load_list, save_list


def add_item(name, price):
    """
    Добавляет товар в список.
    """
    items = load_list()

    items.append({
        "name": name,
        "price": float(price)
    })

    save_list(items)

    print(f"✓ Added: {name} ({price} EUR)")


def show_list():
    """
    Показывает список покупок.
    """
    items = load_list()

    if not items:
        print("Shopping list is empty.")
        return

    print("Shopping list:")
    for i, item in enumerate(items, start=1):
        print(f"  {i}. {item['name']} — {item['price']:.2f} EUR")


def total():
    """
    Считает общую сумму.
    """
    items = load_list()

    total_price = sum(item["price"] for item in items)

    print(f"Total: {total_price:.2f} EUR ({len(items)} items)")


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
        if len(args) != 4:
            print("Usage: add <name> <price>")
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