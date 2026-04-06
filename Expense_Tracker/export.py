import csv


def export_to_csv(expenses, filepath):
    """
    Export expenses to a CSV file.

    Args:
        expenses (list): List of expense dictionaries
        filepath (str): Output file path
    """

    with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        # Header row
        writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])

        # Data rows
        for e in expenses:
            writer.writerow([
                e.get("date", ""),
                f"{e.get('amount', 0):.2f}",
                e.get("category", ""),
                e.get("description", ""),
            ])