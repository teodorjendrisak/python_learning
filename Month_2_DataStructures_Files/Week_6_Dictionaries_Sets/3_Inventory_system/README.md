# Assignment – Week 6, Program Idea #3: Inventory System

## Objective

Practice using Python dictionaries to track and update quantities of items in an inventory.

---

## Requirements

1. Start with an empty dictionary called `inventory`.
2. Allow the user to:
   - **Add** an item with a quantity.
   - **Update** the quantity of an existing item.
   - **Remove** an item completely.
   - **View** the full inventory.
3. Each item name should be the **key**, and its quantity the **value**.
4. Prevent invalid states:
   - No negative quantities allowed.
   - Removing an item that doesn’t exist should show an error message.
5. Program runs in a loop until the user chooses to exit.

---

## Stretch Goals (Optional)

- Save the inventory to a file (`inventory.txt`) when exiting.
- Load the inventory from the file at startup.
- Add a search function (check if item exists and show its quantity).
- Display inventory sorted alphabetically by item name.
- Add a menu-driven system with clear options for the user.

---

## Hints

- Use a `while True:` loop with a menu for repeated operations.
- Use `dict.get(item, 0)` to handle missing items gracefully.
- Use input validation to handle numbers safely (`int()` conversion with try/except).
- Think about using functions (`add_item()`, `remove_item()`, etc.) to keep code organized.
