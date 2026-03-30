import json
import os

# 📁 Файлы
SHOPPING_FILE = "shopping.json"
PRICES_FILE = "prices.json"


# =========================
# 🛒 Работа со списком покупок
# =========================

def load_list():
    """
    Загружает список покупок из shopping.json.
    Если файла нет или он пустой — возвращает [].
    """
    if not os.path.exists(SHOPPING_FILE):
        return []

    try:
        with open(SHOPPING_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_list(items):
    """
    Сохраняет список покупок в shopping.json.
    """
    with open(SHOPPING_FILE, "w", encoding="utf-8") as file:
        json.dump(items, file, indent=2, ensure_ascii=False)


# =========================
# 💰 Работа с ценами
# =========================

def load_prices():
    """
    Загружает цены из prices.json.
    Если файла нет — возвращает пустой словарь {}.
    """
    if not os.path.exists(PRICES_FILE):
        return {}

    try:
        with open(PRICES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


def save_prices(prices):
    """
    Сохраняет словарь цен в prices.json.
    """
    with open(PRICES_FILE, "w", encoding="utf-8") as file:
        json.dump(prices, file, indent=2, ensure_ascii=False)


def get_price(name):
    """
    Возвращает цену товара по имени.
    Если товара нет — возвращает None.
    """
    prices = load_prices()
    return prices.get(name)


def set_price(name, price):
    """
    Добавляет или обновляет цену товара.
    """
    prices = load_prices()
    prices[name] = price
    save_prices(prices)