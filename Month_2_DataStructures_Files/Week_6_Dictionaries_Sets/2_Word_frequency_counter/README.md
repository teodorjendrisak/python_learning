# Assignment – Week 6, Program Idea #2: Word Frequency Counter

## Objective

Learn how to use Python dictionaries to count occurrences of words in a given text.

---

## Requirements

1. Ask the user to input a block of text (multi-line support).
2. Convert all words to lowercase for uniformity.
3. Remove punctuation so words aren’t split incorrectly (e.g., "end." vs "end").
4. Store each unique word as a **key** in a dictionary, with the value being the count of appearances.
5. Print the dictionary in a readable way:
   - One word per line.
   - Word followed by its frequency.
6. Sort the output:
   - First by frequency (highest → lowest).
   - If two words have the same frequency, sort alphabetically.

---

## Stretch Goals (Optional)

- Allow the program to read text from a file instead of user input.
- Output the results to a new file called `word_count.txt`.
- Ignore common “stop words” like: `the, and, a, to, of, in`.
- Show only the top 10 most frequent words.

---

## Hints

- Use `split()` to break text into words.
- Use `str.strip()` and `str.lower()` for cleaning.
- Use `collections.Counter` (optional advanced tool) to simplify counting.
- Use `sorted(dictionary.items(), key=…)` for sorting by frequency.
