# 1_Phonebook_app - Teodor

def main():
    phonebook = {
    "Alice Johnson": "1234567890",
    "Bob Smith": "9876543210",
    "Charlie Brown": "5551234567",
    "Diana Prince": "4449876543",
    "Ethan Hunt": "3332221111"
    }

    menu()

def menu():
    print("1. Add contact" \
    "2. Lookup contact" \
    "3. Update contact" \
    "4. Delete contact" \
    "5. List contacts" \
    "6. Exit")


if __name__ == "__main__":
    main()
