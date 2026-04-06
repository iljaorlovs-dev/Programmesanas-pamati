from datetime import datetime

def filter_by_month(expenses, year, month):
    """
    Return expenses for a specific year and month.

    Args:
        expenses (list): List of expense dictionaries
        year (int): Year to filter
        month (int): Month to filter

    Returns:
        list: Filtered expenses
    """

    result = []

    for expense in expenses:
        # Convert string to datetime
        d = datetime.strptime(expense["date"], "%Y-%m-%d")

        # Check year and month
        if d.year == year and d.month == month:
            result.append(expense)

    return result





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
    


#TOTALS dictionary to store totals for each category
def sum_by_category(expenses):
    """
    Calculate total amount per category.

    Args:
        expenses (list): List of expense dictionaries

    Returns:
        dict: {category: total_amount}
    """

    totals = {}

    for expense in expenses:
        # Get category and amount safely
        category = expense.get("category", "Cits")
        amount = expense.get("amount", 0)

        # If category already exists → add
        if category in totals:
            totals[category] += amount
        else:
            # If not → create new entry
            totals[category] = amount

    # Round values to 2 decimal places
    for cat in totals:
        totals[cat] = round(totals[cat], 2)

    return totals



def get_available_months(expenses):
    """
    Return a sorted list of unique months (YYYY-MM) from expenses.

    Args:
        expenses (list): List of expense dictionaries

    Returns:
        list: Sorted list of months as strings
    """

    months = set()

    for expense in expenses:
        date_str = expense.get("date", "")

        # Extract YYYY-MM
        if len(date_str) >= 7:
            month = date_str[:7]
            months.add(month)

    # Return sorted list
    return sorted(months)