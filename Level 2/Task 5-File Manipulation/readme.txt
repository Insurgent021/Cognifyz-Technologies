# Word Count in File

This Python program counts the occurrences of each word in a given text file and prints the word counts in alphabetical order.

## Features

- Reads a text file and counts the occurrences of each word.
- Ignores punctuation and case, treating "Word" and "word" as the same.
- Prints the word counts sorted in alphabetical order.

## How to Use

1. Save the code in a file named `word_count.py`.
2. Replace `filename` in the example usage section with the path to your text file.
3. Run the program.

## Requirements

- Python 3.x

## Code Explanation

- The program uses the `re` module for regular expression operations to identify words and the `collections` module to count word occurrences.
- It reads the file line by line, converts each line to lowercase, and finds all words using a regular expression.
- The word counts are stored in a `defaultdict` and then sorted by word.
- Finally, the word counts are printed.

## Example Usage

1. Prepare a text file (e.g., `test.txt`) with some text.
2. Run the program using the following command:

   ```python
   python word_count.py

Given a file test.txt with the following content:
Hello world! This is a test file.
This file is used to test the word count program.

The output will be:
a: 1
count: 1
file: 2
hello: 1
is: 2
program: 1
test: 2
the: 1
this: 2
to: 1
used: 1
word: 1
world: 1


## Notes
Ensure the text file is in the same directory as the Python script or provide the full path to the file.
The program considers words to be sequences of alphanumeric characters separated by non-alphanumeric characters.
