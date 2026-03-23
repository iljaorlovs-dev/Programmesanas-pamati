# validators.py

def is_email(text):
    """Check if the text is a simple valid email.

    Conditions:
        - contains '@'
        - contains '.'
        - '@' is not first or last
        - '.' comes after '@'

    Args:
        text: string to validate

    Returns:
        bool: True if valid email, otherwise False

    Example:
        >>> is_email("anna@inbox.lv")
        True
    """
    if not isinstance(text, str):
        return False

    if "@" not in text or "." not in text:
        return False

    if text.startswith("@") or text.endswith("@"):
        return False

    at_index = text.find("@")
    dot_index = text.rfind(".")

    if dot_index < at_index:
        return False

    return True


def is_phone_number(text):
    """Check if the text is a valid Latvian phone number.

    Format:
        +371 XXXXXXXX (8 digits)

    Args:
        text: string to validate

    Returns:
        bool: True if valid phone number, otherwise False

    Example:
        >>> is_phone_number("+371 26123456")
        True
    """
    if not isinstance(text, str):
        return False

    if not text.startswith("+371 "):
        return False

    number_part = text[5:]  # part after "+371 "

    if len(number_part) != 8:
        return False

    if not number_part.isdigit():
        return False

    return True


def is_valid_age(age):
    """Check if age is valid (0–150).

    Args:
        age: integer value

    Returns:
        bool: True if valid age, otherwise False

    Example:
        >>> is_valid_age(25)
        True
    """
    if not isinstance(age, int):
        return False

    if age < 0 or age > 150:
        return False

    return True


def is_strong_password(text):
    """Check if password is strong.

    Conditions:
        - at least 8 characters
        - contains letters
        - contains digits

    Args:
        text: password string

    Returns:
        bool: True if strong password, otherwise False

    Example:
        >>> is_strong_password("abc12345")
        True
    """
    if not isinstance(text, str):
        return False

    if len(text) < 8:
        return False

    has_letter = False
    has_digit = False

    for char in text:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True

    return has_letter and has_digit


def is_valid_date(text):
    """Check if date is in YYYY-MM-DD format (basic validation).

    Args:
        text: string date

    Returns:
        bool: True if valid format, otherwise False

    Example:
        >>> is_valid_date("2024-03-10")
        True
    """
    if not isinstance(text, str):
        return False

    parts = text.split("-")

    if len(parts) != 3:
        return False

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False

    month = int(month)
    day = int(day)

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    return True


# --- Tests ---
if __name__ == "__main__":

    print("--- Email tests ---")
    print(is_email("anna@inbox.lv"))   # True
    print(is_email("anna"))            # False
    print(is_email("anna@"))           # False

    print("\n--- Phone tests ---")
    print(is_phone_number("+371 26123456"))  # True
    print(is_phone_number("26123456"))       # False
    print(is_phone_number("+371 123"))       # False

    print("\n--- Age tests ---")
    print(is_valid_age(25))   # True
    print(is_valid_age(-1))   # False
    print(is_valid_age(200))  # False

    print("\n--- Password tests ---")
    print(is_strong_password("abc12345"))   # True
    print(is_strong_password("abcdefg"))    # False
    print(is_strong_password("12345678"))   # False

    print("\n--- Date tests ---")
    print(is_valid_date("2024-03-10"))  # True
    print(is_valid_date("2024-13-10"))  # False
    print(is_valid_date("2024-03"))     # False