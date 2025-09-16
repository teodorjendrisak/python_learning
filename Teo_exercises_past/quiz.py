
QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is 5 * 6?",
        "options": ["11", "30", "56", "20"],
        "answer": "30"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Gold", "Silver", "Iron"],
        "answer": "Oxygen"
    },
    {
        "question": "What year did the Titanic sink?",
        "options": ["1912", "1905", "1898", "1920"],
        "answer": "1912"
    },
    {
        "question": "Which language is primarily spoken in Brazil?",
        "options": ["Spanish", "Portuguese", "French", "English"],
        "answer": "Portuguese"
    },
    {
        "question": "What is the square root of 144?",
        "options": ["10", "12", "14", "16"],
        "answer": "12"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    }
]

def main():
    print("\nWelcome to a simple quizz.\nYou will be presented with 10 multiple choice questions.\n")
    input("Press ENTER to start \n")
    final_score = quiz()
    print(f"Thank you for taking this short quiz.\nYour final score is {final_score}/10.\n{score_assessment(final_score)}")
    input("Press ENTER to exit ")

def quiz():
    letters = ["A", "B", "C", "D"]
    score = 0

    for q in QUESTIONS:
        print(q["question"])

        #Link option to a letter
        for letter, option in zip(letters, q["options"]):
            print(f"{letter}) {option}")
        player_answer = get_valid_answer()
        if check_answer(q, player_answer, letters):
            score += 1
        print(f"Current score: {score}/10\n")
        print("-" *40)
        input("Press ENTER to continue\n")
    return score

def get_valid_answer():
    while True:
        answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Please input valid answer (A, B, C, or D)")

def check_answer(q, player_answer, letters):
    idx = letters.index(player_answer)
    selected_option = q["options"][idx]

    if selected_option == q["answer"]:
        print("\nCorrect!")
        return True
    else:
        print(f"\nWrong!\nCorrect answer is {q["answer"]}")
        return False

def score_assessment(final_score):
    if final_score == 10:
        return "Perfect score! Outstanding!"
    elif final_score >= 8:
        return "Great job! You really know your stuff."
    elif final_score >= 5:
        return "Good effort! Keep practicing."
    elif final_score >= 3:
        return "Not bad, but you can improve."
    else:
        return "U suck"

if __name__ == "__main__":
    main()