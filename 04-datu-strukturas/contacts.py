import sys
import json
import os

#contacts file name
CONTACTS_FILE = "contacts.json"

#autocreate json file if it doesn't exist
if not os.path.exists(CONTACTS_FILE):
    save_contacts([])

#contacts loading

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []

    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    

#contacts saving
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)




#contacts adding
def add_contact(name, phone):
    contacts = load_contacts()

    contacts.append({
        "name": name,
        "phone": phone
    })

    save_contacts(contacts)

    print(f"✓ Pievienots: {name} ({phone})")



    #list all contacts
def list_contacts():
    contacts = load_contacts()

    if not contacts:
        print("Kontaktu nav.")
        return

    print("Kontakti:")
    for i, contact in enumerate(contacts, start=1):
        print(f"  {i}. {contact['name']} — {contact['phone']}")



#contacts searching
def search_contacts(query):
    contacts = load_contacts()

    results = []

    for contact in contacts:
        if query.lower() in contact["name"].lower():
            results.append(contact)

    print(f"Atrasti {len(results)} kontakti:")

    for i, contact in enumerate(results, start=1):
        print(f"  {i}. {contact['name']} — {contact['phone']}")


#CLI added
if __name__ == "__main__":
    command = sys.argv[1]

    if command == "add":
        name = sys.argv[2]
        phone = sys.argv[3]
        add_contact(name, phone)

    elif command == "list":
        list_contacts()

    elif command == "search":
        query = sys.argv[2]
        search_contacts(query)

    else:
        print("Nezināma komanda.")
