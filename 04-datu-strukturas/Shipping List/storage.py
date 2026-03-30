import json
import os

FILE_NAME = "shopping.json"
PRICES_FILE = "prices.json"


#prices file
def load_prices():
    if not os.path.exists(PRICES_FILE):
        return {}

    try:
        with open(PRICES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}



def save_prices(prices):
    with open(PRICES_FILE, "w", encoding="utf-8") as file:
        json.dump(prices, file, indent=2, ensure_ascii=False)


def get_price(name):
    prices = load_prices()
    return prices.get(name)


def set_price(name, price):
    prices = load_prices()
    prices[name] = price
    save_prices(prices)




def load_list():
    """
    Загружает список покупок из файла.
    Если файл пустой или сломан — возвращает пустой список.
    """
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_list(items):
    """
    Сохраняет список покупок в файл.
    """
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(items, file, indent=2, ensure_ascii=False)