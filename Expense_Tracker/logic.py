def sum_total(expenses):
    """
    Calculate the total sum of all expenses.

    Args:
        expenses (list): A list of expense dictionaries.
                         Each dictionary must contain an "amount" key.

    Returns:
        float: Total sum of all expense amounts.
    """

    # Step 1: Initialize total sum variable
    total = 0.0

    # Step 2: Loop through each expense in the list
    for expense in expenses:

        # Step 3: Get the amount value from the dictionary
        # Using .get() to avoid crashing if key is missing
        amount = expense.get("amount", 0)

        # Step 4: Add amount to total sum
        total += amount

    # Step 5: Round result to 2 decimal places (money format)
    return round(total, 2)


from datetime import datetime


#datetime module
def is_valid_date(text):
    """
    Check if the given string is a valid date in YYYY-MM-DD format.

    Args:
        text (str): Date string entered by the user.

    Returns:
        bool: True if valid, False otherwise.
    """

    try:
        # Try to parse the string into a date
        datetime.strptime(text, "%Y-%m-%d")
        return True

    except ValueError:
        # If parsing fails → invalid date
        return False