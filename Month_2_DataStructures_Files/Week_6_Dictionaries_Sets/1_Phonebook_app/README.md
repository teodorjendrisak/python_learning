# 1 Phonebook app

**Assignment:** Build a Phonebook App using Python dictionaries.

**Requirements**
Create a dictionary where keys are names (strings) and values are phone numbers (strings or integers).

**Implement the following functionality:**
Add contact: Ask the user for a name and a number, then store it in the dictionary.
Lookup contact: Ask the user for a name, print the number if found, otherwise print "Not found".
Update contact: If a name already exists, allow updating the stored number.
Delete contact: Allow removing a name/number pair from the dictionary.
List contacts: Print all stored names and numbers, sorted alphabetically by name.
Store at least 5 contacts at the start of the program so the dictionary is never empty.

**Use a simple text menu for interaction, for example:**

1. Add contact
2. Lookup contact
3. Update contact
4. Delete contact
5. List contacts
6. Exit

**Constraints**
Use only dictionaries, no external libraries.
Input must be handled safely (e.g., don’t crash if name not found).
Loop until the user chooses Exit.

**Stretch Goals**
Make phone numbers accept only digits.
Prevent duplicate names (ask user if they want to update instead).
Save and load contacts from a text file (phonebook.txt) so the app remembers data between runs.

Dummy phonebook dictionary:

phonebook = {
"Alice Johnson": "1234567890",
"Bob Smith": "9876543210",
"Charlie Brown": "5551234567",
"Diana Prince": "4449876543",
"Ethan Hunt": "3332221111"
}
