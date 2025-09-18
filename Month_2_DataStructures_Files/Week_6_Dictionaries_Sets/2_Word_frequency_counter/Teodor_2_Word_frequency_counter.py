# 2_Word_frequency_counter - Teodor
import string
from collections import Counter

def load_input_file():
    with open("Teodor_input.txt", "r") as file:
        contents = file.readlines() #New learning from chat
    return contents


def process_text(text):
    #Merge lines of text into 1 string
    text = " ".join(text)

    #Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    #Split text into lowered words
    words = text.lower().split()

    return(words)


def word_count(words):
    #THIS WAS MY SOLUTION
    # words_count = {}
    # for word in words:
    #     if word in ["the", "and", "a", "to", "of", "in"]:
    #         continue
    #     else:
    #         if word not in words_count:
    #             words_count[word] = 1
    #         else:
    #             words_count[word] += 1

    #THIS IS WHAT CHATGPT TAUGHT ME AFTER
    words_count = Counter(words)

    return words_count


def print_counter(words_count):
    #This is new to me and explained by ChatGPT
    sorted_words = sorted(words_count.items(), key=lambda x: (-x[1], x[0]))
    print("-" * 30)
    for word, count in sorted_words[:10]:
        print(f"{word}: {count}")
    print("-" * 30)


def main():
    while True:
        input_choice = input("Do you want to use input.txt or enter text manually? (FILE/SELF) ").upper()

        if input_choice == "FILE":
            contents = load_input_file()
            break

        elif input_choice == "SELF":
            contents = []
            print("Enter/Paste your text. Type 'END' on a new line to finish.")

            while True:
                line = input()
                if line == "END":
                    break
                contents.append(line)
            break
        else:
            print("Please choose a valid option.")

    words = process_text(contents)
    words_count = word_count(words)
    print_counter(words_count)

if __name__ == "__main__":
    main()