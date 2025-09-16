import random
import os
import time


def main():
    participants = participant_collection()
    assignments = assign_recipients(participants)
    assignments_normalized = {giver.casefold(): receiver for giver, receiver in assignments.items()}
    receiver_reveal(assignments_normalized)


def participant_collection():
    participants = []
    while True:
        name = input("Enter participant name (or type 'DONE' to finish) ").strip()
        if name.lower() == "done":
            if len(participants) < 3:
                print("Not enough names in the list")
                continue
            else:
                return participants
        participants.append(name.capitalize())

def assign_recipients(participants):
    while True:
        recipients = participants[:]
        random.shuffle(recipients)
        if all(giver != receiver for giver, receiver in zip(participants, recipients)):
            return dict(zip(participants, recipients))

def receiver_reveal(assignments_normalized):
    while True:
        current_giver = input("Type your name to find out who you're buying a present for (or type 'DONE' to finish) ").strip()
        current_giver_cf = current_giver.casefold()
        if current_giver_cf in assignments_normalized:
            print(f"\nYou are buying a gift for {assignments_normalized[current_giver_cf]}\n")
            ### This is an option for clearing the screen manually
            # input("Press ENTER to continue... ")
            clear_screen()
        elif current_giver_cf == "done":
            return
        else:
            print("Your name is not on the list. Please type a name from the list")

def clear_screen(delay=5):
    for remaining in range(delay, 0, -1):
        print(f"\r ***The screen will clear in {remaining} seconds***\033[K", end="")
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()