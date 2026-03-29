import json
import os

FILE_NAME = "shopping.json"


def load_list():
    """
    Загружает список покупок из файла.
    Если файла нет — возвращает пустой список.
    """
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_list(items):
    """
    Сохраняет список покупок в файл.
    """
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(items, file, indent=2, ensure_ascii=False)