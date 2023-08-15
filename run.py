import random
from wordlist import word_list

def choose_word():
    """
    Function that chooses a random word from the wordlist
    and returns it in uppercase for better readability
    """
    word = random.choice(word_list)
    return word.upper()

def init_game():
    """
    Function that initializes game when user accepts to play
    """
    roundstart = input("Welcome to Hangman! Do you think you can rescue the poor man from hanging? y/n \n")
    if roundstart == "y":
        print("Let's play!")
    elif roundstart == "n":
        print("What a pitty! Maybe you will change your mind and come to play soon.")
    else:
        #raise ValueError("Answer must be 'n' or 'y'")
        print("Answer must be 'n' or 'y'")
        init_game()


#def start_game():
#    correct_guesses = []
#    incorrect_guesses = []
#    tries = 6



# Hangman ASCII art source: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
def display_hangman(tries):
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
    return phases[tries]

def main():
    """
    Run all program functions
    """
    choose_word()

#main()

init_game()