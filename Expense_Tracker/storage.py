import json
import os

# Name of the file where all expenses will be stored
FILE_NAME = "expenses.json"


def load_expenses():
    """
    Load expenses from a JSON file.

    Returns:
        list: A list of expense dictionaries.
              If the file does not exist or is invalid, returns an empty list.
    """

    # Step 1: Check if the file exists
    # If not, there is nothing to load → return empty list
    if not os.path.exists(FILE_NAME):
        return []

    try:
        # Step 2: Open the file in read mode with UTF-8 encoding
        with open(FILE_NAME, "r", encoding="utf-8") as f:

            # Step 3: Convert JSON data into Python object (usually a list)
            data = json.load(f)

            # Step 4: Validate that the data is actually a list
            # This protects against corrupted or unexpected file structure
            if isinstance(data, list):
                return data
            else:
                # If data is not a list → return empty list as fallback
                return []

    except (json.JSONDecodeError, IOError):
        # Step 5: Handle errors safely
        # JSONDecodeError → file is corrupted (invalid JSON)
        # IOError → file cannot be read
        # In both cases, return empty list instead of crashing the program
        return []


def save_expenses(expenses):
    """
    Save expenses to a JSON file.

    Args:
        expenses (list): A list of expense dictionaries to save.
    """

    # Step 1: Open the file in write mode
    # "w" means the file will be overwritten each time
    with open(FILE_NAME, "w", encoding="utf-8") as f:

        # Step 2: Convert Python object (list) into JSON and write to file
        json.dump(
            expenses,   # data to save
            f,          # file object
            ensure_ascii=False,  # keep non-English characters (e.g., Ē, ā)
            indent=2    # format JSON with indentation for readability
        )