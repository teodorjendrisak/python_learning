import random
import os
import unicodedata # This was given to me by ChatGPT, I don't understand it yet


VOCABULARY = [
    {"slovak": "jablko", "romanian": "măr"},          # apple
    {"slovak": "chlieb", "romanian": "pâine"},        # bread
    {"slovak": "voda", "romanian": "apă"},            # water
    {"slovak": "mlieko", "romanian": "lapte"},        # milk
    {"slovak": "kniha", "romanian": "carte"},         # book
    {"slovak": "stôl", "romanian": "masă"},           # table
    {"slovak": "stolička", "romanian": "scaun"},      # chair
    {"slovak": "dom", "romanian": "casă"},            # house
    {"slovak": "dvere", "romanian": "ușă"},           # door
    {"slovak": "okno", "romanian": "fereastră"},      # window
    {"slovak": "auto", "romanian": "mașină"},         # car
    {"slovak": "vlak", "romanian": "tren"},           # train
    {"slovak": "pes", "romanian": "câine"},           # dog
    {"slovak": "mačka", "romanian": "pisică"},        # cat
    {"slovak": "ryba", "romanian": "pește"},          # fish
    {"slovak": "mesto", "romanian": "oraș"},          # city
    {"slovak": "škola", "romanian": "școală"},        # school
    {"slovak": "učiteľ", "romanian": "profesor"},     # teacher
    {"slovak": "dieťa", "romanian": "copil"},         # child
    {"slovak": "priateľ", "romanian": "prieten"}      # friend
]

def main():
    print("Welcome to the language flashcard program\n")
    language = language_selection()
    score = flashcards(language)
    results(score)
    input("Press ENTER to exit ")

def language_selection():
    while True:
        user_lang_select = input("Do you want to practice Romanian or Slovak? (R/S): ").strip().upper()
        if user_lang_select in ("R", "S"):
            print("Selection complete")
            return user_lang_select
        else:
            print("Please input valid answer (R or S)")

def flashcards(language):
    if language == "R":
        question_key, answer_key = "slovak", "romanian"
    else:
        question_key, answer_key = "romanian", "slovak"
    score = 0

    vocabulary_shuffle = VOCABULARY[:]
    random.shuffle(vocabulary_shuffle)
    for card in vocabulary_shuffle:
        question = card[question_key]
        correct_answer = card[answer_key]
        user_answer = input(f"\nHow do you say {question}? ").strip().lower()

        if user_answer == correct_answer or normalize(user_answer) == normalize(correct_answer):
            print("\nCorrect!\n")
            score += 1
        else:
            print("\nIncorrect answer")
            print(f"Correct answer is: {correct_answer}\n")
            user_peek_a = user_peek_q()
            if user_peek_a == "Y":
                dictionary_peek(question_key, answer_key)
        print("-" *40)
    return score

def results(score):
    result_percentage = round((score / len(VOCABULARY)) * 100)
    print(f"Final score: {result_percentage}%")
    if result_percentage == 100:
        print("Perfect! You nailed every word.")
    elif result_percentage >= 80:
        print("Great job! Strong vocabulary skills.")
    elif result_percentage >= 60:
        print("Good effort, you're getting there.")
    elif result_percentage >= 40:
        print("Not bad, but more practice is needed.")
    else:
        print("Needs improvement. Keep practicing.")

def user_peek_q():
    while True:
        answer_peek = input("Do you want to peek into the dictionary before the next question? (Y/N): ").strip().upper()
        if answer_peek in ["Y", "N"]:
            return answer_peek
        else:
            print("Please enter a valid option: Y for yes or N for no. ")

def dictionary_peek(question_key, answer_key):
    print("-" *40)
    for pair in VOCABULARY:
        print(f"{pair[question_key]} - {pair[answer_key]}")
    print("-" *40)
    input("\nPress ENTER to continue ")
    clear_console()

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def normalize(text):  # This was given to me by ChatGPT, I don't understand it yet
    """Convert text to ASCII-only lowercase, ignoring diacritics (for user input comparison)."""
    return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode().lower()


if __name__ == "__main__":
    main()