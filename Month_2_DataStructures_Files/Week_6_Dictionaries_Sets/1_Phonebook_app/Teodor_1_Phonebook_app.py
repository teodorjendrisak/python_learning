# 1_Phonebook_app - Teodor


def load_phonebook():
    phonebook = {}
    with open("Teodor_phonebook.txt", "r") as file:
        for line in file:
            name, number = line.strip().split(":")
            phonebook[name] = number
    return phonebook


def save_phonebook(phonebook):
    with open("Teodor_phonebook.txt", "w") as file:
        for name, number in phonebook.items():
            file.write(f"{name}:{number}\n")


def menu_selection():
    print("\nMENU\n"
    "1. Add contact\n"
    "2. Lookup contact\n"
    "3. Update contact\n"
    "4. Delete contact\n"
    "5. List contacts\n"
    "6. Exit\n")

    while True:
        try:
            choice = int(input("Select action: "))
            if 0 < choice < 7:
                return choice
            else:
                print("Please choose from the menu items")
        except ValueError:
            print("Please enter valid number")


def add_contact(phonebook):
    name = input("Full name: ")

    #Check if the name exists
    if name in phonebook:
        while True:
            choice_update = input("The name already exists in the phonebook. Do you want to update instead? (Y/N): ").upper()
            if choice_update == "Y":
                update_contact(name, phonebook)
                return
            elif choice_update == "N":
                return
            else:
                print("Please enter a valid response")

    while True:
        number = input("Number: ")
        if number.isdigit():
            phonebook[name] = number
            input("Contact added. Press ENTER to return to the main menu ")
            print("-" * 30)
            return
        else:
            print("Only digits accepted for phone numbers")


def lookup_contact(phonebook):
    name = input("Full name of the contact to look up: ")

    if name in phonebook:
        print(f"\n{phonebook[name]}\n")
    else:
        print("Name not found in the phonebook")

    input("Press ENTER to return to main menu ")
    print("-" * 30)
    return


def update_contact(name, phonebook):
    if name == "":
        name = input("Full name of the contact to update: ")

    ### Can add that lowered input gets compared for case-sensitivity
    if name in phonebook:
        while True:
            number_update =input("New number: ")
            if number_update.isdigit():
                phonebook[name] = number_update
                input("Number updated. Press ENTER to return to the main menu")
                print("-" * 30)
                return
            else:
                print("Only digits accepted for numbers") 
    else:
        print("Name not found in the phone book")
        input("Press ENTER to return to the main menu ")
        print("-" * 30)
        return


def delete_contact(phonebook):
    name = input("Full name of the contact to delete: ")
    if name in phonebook:
        del phonebook[name]
        print("Name deleted")
    else:
        print("Name not found in the phonebook")

    input("Press ENTER to return to the main menu ")
    print("-" * 30)
    return


def list_contacts(phonebook):
    phonebook_sorted = sorted(phonebook.items())
    print("-" * 30)
    for name, number in phonebook_sorted:
        print(f"{name}: {number}")
    print("-" * 30)
    input("Press ENTER to return to the main menu ")


def main():
    phonebook = load_phonebook()

    while True:
        menu_choice = menu_selection()
        if menu_choice == 1:
            add_contact(phonebook)
        elif menu_choice == 2:
            lookup_contact(phonebook)
        elif menu_choice == 3:
            update_contact("", phonebook)
        elif menu_choice == 4:
            delete_contact(phonebook)
        elif menu_choice == 5:
            list_contacts(phonebook)
        elif menu_choice == 6:
            save_phonebook(phonebook)
            return


if __name__ == "__main__":
    main()