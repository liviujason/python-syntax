words = ["hello", "mate", "lovely", "day", "we're", "having"]

for word in words:
    print(word.upper())


def print_upper_words(words, char, second_char):
    """Prints the all capitalized version of each word from a list of words"""

    for word in words:
        if word[0] == char or word[0] == char.upper() or word[0] == second_char or word[0] == second_char.upper():
            print(word.upper())
