# 3_Inventory_system - Teodor
def load_inventory():
    inventory = {}
    try:
        with open("Teodor_inventory.txt", "r") as file:
            for line in file:
                try:
                    item, quantity = line.strip().split(":")
                    inventory[item] = int(quantity)
                except ValueError:
                    continue
    except FileNotFoundError:
        pass     
    return inventory


def save_inventory(inventory):
    with open("Teodor_inventory.txt", "w") as file:
        for item in inventory:
            file.write(f"{item}: {inventory[item]}\n")


def menu_selection():
    print("\nMENU\n"
    "1. Add item\n"
    "2. Update item\n"
    "3. Remove item\n"
    "4. Search item\n"
    "5. View inventory\n"
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


def add_item(inventory):
    #Check if the item exists
    item = input("Item: ")

    if item in inventory:
        while True:
            choice_update = input("The item already exists in the inventory. Do you want to update instead? (Y/N): ").upper()
            if choice_update == "Y":
                update_item(item, inventory)
                return
            elif choice_update == "N":
                return
            else:
                print("Please enter a valid response")

    while True:
        quantity = input("Quantity: ")
        if quantity.isdigit():
            inventory[item] = int(quantity)
            input("Item added. Press ENTER to return to the main menu ")
            print("-" * 30)
            return
        else:
            print("Only digits accepted for quantity")


def update_item(item, inventory):
    if item == "":
        item = input("Item to update: ").strip()


    if item in inventory:
        while True:
            quantity_update =input("Quantity to add: ")
            if quantity_update.isdigit() and int(quantity_update) > 0:
                inventory[item] += int(quantity_update)
                input("Quantity updated. Press ENTER to return to the main menu")
                print("-" * 30)
                return
            else:
                print("Only positive numbers accepted") 
    else:
        print("Item not found in the inventory")
        input("Press ENTER to return to the main menu ")
        return


def remove_item(inventory):
    while True:
        item = input("Item to delete: ")
        if item in inventory:
            try:
                choice = int(input("Quantity to remove (type 0 for complete removal): "))
                if choice == 0:
                    del inventory[item]
                    print("Item deleted")
                    break
                elif choice > 0:
                    if choice < inventory[item]:
                        inventory[item] -= choice
                        print("Quantity updated")
                        break
                    elif choice == inventory[item]:
                        del inventory[item]
                        print("Quantity is 0, item deleted")
                        break
                    else:
                        print("Quantity to remove is higher than current quantity")
                        print(f"Current quantity: {inventory[item]}")
                        break
                else:
                    print("Please enter a positive number")
            except ValueError:
                print("Please enter a number")
        else:
            print("Item not found in the inventory")
            break

    input("Press ENTER to return to the main menu ")
    print("-" * 30)


def search_item(inventory):
    search = input("Search item: ").strip().lower()
    for item in inventory:
        if item.lower() == search:
            print(f"{item}: {inventory[item]}")
            input("Press ENTER to return to the main menu ")
            return
    print("Item not found in the inventory")
    input("Press ENTER to return to the main menu ")


def view_inventory(inventory):

    for item in sorted(inventory.keys()):
        print(f"{item}: {inventory[item]}")
    input("Press ENTER to return to the main menu ")
    return


def main():
    inventory = load_inventory()

    while True:
        menu_choice = menu_selection()
        if menu_choice == 1:
            add_item(inventory)
        elif menu_choice == 2:
            update_item("", inventory)
        elif menu_choice == 3:
            remove_item(inventory)
        elif menu_choice == 4:
            search_item(inventory)
        elif menu_choice == 5:
            view_inventory(inventory)
        elif menu_choice == 6:
            save_inventory(inventory)
            break



if __name__ == "__main__":
    main()
    