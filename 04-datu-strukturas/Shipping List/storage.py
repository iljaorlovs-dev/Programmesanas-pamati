import json
import os

FILE_NAME = "shopping.json"


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