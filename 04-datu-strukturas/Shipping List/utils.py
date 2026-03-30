def calc_line_total(item):
    """
    Возвращает сумму для одного товара: qty * price
    """
    return item["qty"] * item["price"]


def calc_grand_total(items):
    """
    Считает общую сумму всех товаров
    """
    return sum(calc_line_total(item) for item in items)


def count_units(items):
    """
    Считает общее количество единиц товаров
    """
    return sum(item["qty"] for item in items)