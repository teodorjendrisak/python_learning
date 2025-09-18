# Assignment – Week 6, Program Idea #5: Unique Word Finder with Sets

## Objective

Practice using Python sets to identify unique words from a block of text.

---

## Requirements

1. Ask the user to input a block of text.
2. Convert all words to lowercase for uniformity.
3. Remove punctuation so words are not treated as different (e.g., `"end."` vs `"end"`).
4. Store all words in a **set** to automatically filter duplicates.
5. Print the list of unique words.
6. Display the **count** of unique words at the end.

---

## Stretch Goals (Optional)

- Allow the user to load text from a file instead of typing.
- Output the unique words to a new file called `unique_words.txt`.
- Show the words in alphabetical order.
- Display the 5 longest unique words.
- Ignore common stop words like: `the, and, a, to, of, in`.

---

## Hints

- Use `split()` to break text into words.
- Use `str.lower()` for normalization.
- Use `set()` to eliminate duplicates quickly.
- Use `sorted()` to display words in alphabetical order.
- For punctuation, consider using `str.strip()` or the `string` module (`string.punctuation`).
