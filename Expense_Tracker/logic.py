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