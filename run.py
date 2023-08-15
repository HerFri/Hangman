import random
from wordlist import word_list

def choose_word():
    """
    Function that chooses a random word from the wordlist
    and returns it in uppercase for better readability
    """
    word = random.choice(word_list)
    return word.upper()

def main():
    """
    Run all program functions
    """
    choose_word()

main()