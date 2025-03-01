"""
Word Occurrences
Estimate: 30 minutes
Actual:   45 minutes
"""

def count_word_occurrences(text):
    """Count the occurrences of each word in the given text."""
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def find_longest_word_length(word_counts):
    """Find the length of the longest word in the dictionary."""
    return max(len(word) for word in word_counts.keys())

def print_word_counts(word_counts):
    """Print the word counts sorted alphabetically and aligned neatly."""
    longest_word_length = find_longest_word_length(word_counts)
    for word, count in sorted(word_counts.items()):
        print(f"{word:{longest_word_length}} : {count}")

def main():
    """Main function to run the program."""
    text = input("Text: ")
    word_counts = count_word_occurrences(text)
    print_word_counts(word_counts)


if __name__ == "__main__":
    main()