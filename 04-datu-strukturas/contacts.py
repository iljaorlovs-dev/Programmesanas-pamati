import sys      # used to read command-line arguments
import json     # used to work with JSON (save/load data)
import os       # used to check if file exists

# file name where contacts will be stored
CONTACTS_FILE = "contacts.json"


def load_contacts():
    """
    Load contacts from JSON file.
    If the file does not exist, return an empty list.
    """
    # check if file exists
    if not os.path.exists(CONTACTS_FILE):
        return []

    # open file in read mode ("r")
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        # convert JSON data into Python list
        return json.load(f)


def save_contacts(contacts):
    """
    Save contacts list to JSON file.
    """
    # open file in write mode ("w")
    # creates file if it does not exist
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        # write Python list into JSON format
        json.dump(contacts, f, indent=2, ensure_ascii=False)


def add_contact(name, phone):
    """
    Add a new contact to the list.
    """
    # load existing contacts
    contacts = load_contacts()

    # add new contact (dictionary)
    contacts.append({
        "name": name,
        "phone": phone
    })

    # save updated list back to file
    save_contacts(contacts)

    # print confirmation message
    print(f"✓ Pievienots: {name} ({phone})")


def list_contacts():
    """
    Display all contacts.
    """
    # load contacts
    contacts = load_contacts()

    # if list is empty → show message
    if not contacts:
        print("Kontaktu nav.")
        return

    # print all contacts with numbering
    print("Kontakti:")
    for i, contact in enumerate(contacts, start=1):
        print(f"  {i}. {contact['name']} — {contact['phone']}")


def search_contacts(query):
    """
    Search contacts by name (case-insensitive).
    """
    # load contacts
    contacts = load_contacts()

    results = []

    # check each contact
    for contact in contacts:
        # compare lowercase strings to ignore case
        if query.lower() in contact["name"].lower():
            results.append(contact)

    # print number of found contacts
    print(f"Atrasti {len(results)} kontakti:")

    # print results
    for i, contact in enumerate(results, start=1):
        print(f"  {i}. {contact['name']} — {contact['phone']}")


if __name__ == "__main__":
    # create file automatically if it does not exist
    if not os.path.exists(CONTACTS_FILE):
        save_contacts([])

    # check if user provided a command
    if len(sys.argv) < 2:
        print("Usage: add | list | search")
        sys.exit()

    # read command (first argument)
    command = sys.argv[1]

    if command == "add":
        # check if name and phone are provided
        if len(sys.argv) < 4:
            print('Usage: add "Name" "Phone"')
            sys.exit()

        name = sys.argv[2]
        phone = sys.argv[3]
        add_contact(name, phone)

    elif command == "list":
        list_contacts()

    elif command == "search":
        # check if search query is provided
        if len(sys.argv) < 3:
            print('Usage: search "Name"')
            sys.exit()

        query = sys.argv[2]
        search_contacts(query)

    else:
        print("Unknown command.")