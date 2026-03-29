#contacts loading

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []

    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)