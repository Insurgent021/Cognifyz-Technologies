import re
from collections import defaultdict

def count_words_in_file(filename):
    # Initialize a default dictionary to count word occurrences
    word_counts = defaultdict(int)
    
    # Open and read the file
    with open(filename, 'r') as file:
        for line in file:
            # Use regex to find words, ignoring punctuation and case
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                word_counts[word] += 1

    # Sort the dictionary by keys (words)
    sorted_word_counts = dict(sorted(word_counts.items()))

    # Print the word counts
    for word, count in sorted_word_counts.items():
        print(f'{word}: {count}')


filename = 'test.txt'  # Replace with your file name

# Function execution
count_words_in_file(filename)
