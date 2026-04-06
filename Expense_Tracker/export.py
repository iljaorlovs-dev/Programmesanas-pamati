import csv


def export_to_csv(expenses, filepath):
    """
    Export expenses to a CSV file.

    Args:
        expenses (list): List of expense dictionaries
        filepath (str): Output file path
    """

    try:
        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)

            writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])

            for e in expenses:
                writer.writerow([
                    e.get("date", ""),
                    round(e.get("amount", 0), 2),
                    e.get("category", ""),
                    e.get("description", ""),
                ])

        return True

    except OSError:
        return False