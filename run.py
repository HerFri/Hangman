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


# Hangman ASCII art source: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
def display_hangman(attempts):
    phases = [   '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    return phases[attempts]

main()