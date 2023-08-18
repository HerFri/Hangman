import random
from wordlist import get_word
from hangmanascii import HANG_STAGES
from hangmanascii import HANGMANTITLE
from hangmanascii import YOUWIN
from hangmanascii import YOULOSE
from hangmanascii import RULES


hangman = HANG_STAGES
title = HANGMANTITLE
you_win = YOUWIN
you_lose = YOULOSE

NOT_VALID_LETTERS = ["ä", "ö", "ü", "ß"]

       
def init_game():
    """
    Function that initializes game when user accepts to play
    """
    print(title)
    round_start = input("Welcome to Hangman! Do you think you can rescue the poor man from hanging? Y/N (Press R to read the rules) \n").lower()
    if round_start == "r":
        show_rules()
    elif round_start == "y":
        start_game()
    elif round_start == "n":
        print("What a pitty! Maybe you will change your mind and come back soon to save a man from hanging.")
    else:
        print("Answer must be 'n' or 'y'")
        init_game()

def show_rules():
    """
    Function that displays the rules of the game to the player
    """
    print(RULES)
    ready_to_play()

def ready_to_play():
    """
    Function that asks if the player is ready to play
    """
    ask_to_play = input("Ready to play? Y/N \n").lower()
    if ask_to_play == "y":
        start_game()
    elif ask_to_play == "n":
        print("What a pitty! Maybe you will change your mind and come back soon to save a man from hanging.")
    else:
        print(f"{ask_to_play} is not a valid answer.")
        ready_to_play()


def win_round(word):
    """
    Function that is executed when player guessed the right word
    """
    print(you_win)
    print(f"Splendid! You guessed the right word {word} and saved the man from being hanged!")
    win_next_round = input("Want to save some man's life again? y/n \n")
    if win_next_round == "y":
        start_game()
    elif win_next_round == "n":
        print("What a pitty! Maybe you will change your mind and come to play soon.")


def lose_round(word):
    """
    Function that is executed when player did not guess the right word
    """
    print(you_lose)
    print(f"Game Over! The word was {word}")
    lose_next_round = input("Want to play again? y/n \n")
    if lose_next_round == "y":
        start_game()
    elif lose_next_round == "n":
        print("What a pitty! Maybe you will change your mind and come back to save more men from hanging.")


def start_game():
    """
    Function for starting the actual game, when player agrees to play a game 
    """
    word = get_word()
    
    tries = 6
    
    correct_guesses = []
    incorrect_guesses = []

    hangman_counter = -1     
    

    while tries > 0:
        output = ""
        for letter in word:
            if letter in correct_guesses:
                output += letter
            else:
                output += "_ "
        if output == word:
            break 

        print("Guess a letter of the word: ", output)
        print(tries, " tries left")

        guess = input().lower()
        if not guess.isalpha():
            print(f"{guess} is not a letter!")
            continue
        elif guess in NOT_VALID_LETTERS:
            print(f"{guess} is not a valid letter!")
            continue
        #elif guess == word:
        elif len(guess) > 1:
            print("Pick only one letter!")
            continue

        if guess in correct_guesses or guess in incorrect_guesses:
            print("Already guessed", guess)
        elif guess == word:
            win_round(word)

        elif guess in word:
            print(f"Good job, the letter {guess} is in the word!")
            correct_guesses.append(guess)
       
        else:
            print(f"Unfortunately, {guess} is not in the word. Try again!")
            hangman_counter = hangman_counter + 1
            tries = tries - 1
            incorrect_guesses.append(guess)
            print(hangman[hangman_counter])
    if tries > 0:
        win_round(word)
    elif tries == 0:
        lose_round(word)  
    else:
        print("Sorry you guessed the wrong letter. Try again!")


def main():
    """
    Run all program functions
    """

    
init_game()