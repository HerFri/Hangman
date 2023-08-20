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
    round_start = input("Welcome to Hangman! Do you think you can "
                        "rescue the poor man from hanging? Y/N \n"
                        "(Press R to read the rules) \n").lower()
    if round_start == "r":
        show_rules()
    elif round_start == "y":
        start_game()
    elif round_start == "n":
        print("What a pitty! Maybe you will change your mind "
              "and come back soon to save a man from hanging.")
    else:
        print("Answer must be 'Y','N' or 'R'")
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
        print("What a pitty! Maybe you will change your mind "
              "and come back soon to save a man from hanging.")
    else:
        print(f"{ask_to_play} is not a valid answer.")
        ready_to_play()


def play_again():
    """
    Function that asks the player if another game wants to be played
    """
    next_round = input("Want to play again? Y/N \n")
    if next_round == "y":
        print("Let's play another round!")
        print("\n")
        start_game()
    elif next_round == "n":
        print("What a pitty! Maybe you will change your mind "
              "and come back soon to play again.")
    else:
        print(f"{next_round} is not a valid answer")
        play_again()


def win_round(word):
    """
    Function that is executed when player guessed the right word
    """
    print(you_win)
    print(f"Splendid! You guessed the right word {word} and saved "
          "the man \nfrom being hanged!")
    play_again()


def lose_round(word):
    """F
    Function that is executed when player did not guess the right word
    """
    print(you_lose)
    print(f"Game Over! The word was {word}")
    play_again()


def start_game():
    """
    Function for starting the actual game, when player agrees to play a game
    """
    word = get_word()
    tries = 6
    guessed_letters = []
    hangman_counter = -1

    # for some parts of the code for the while-loop I took inspiration from
    # this tutorial
    # (https://www.youtube.com/watch?v=MtYw0RaZ4B0&ab_channel=NPStation)
    # and reworked/modified the code for additional features
    while tries > 0:
        word_completed = ""
        for letter in word:
            if letter in guessed_letters:
                word_completed += letter
                print(letter, end=" ")
            else:
                print("_", end=" ")

        if word_completed == word:
            win_round(word)
            break

        print("\n")
        print(tries, " tries left")

        if guessed_letters:
            print("Already guessed letters:",
                  *sorted(guessed_letters), sep=" ")

        guess = input("Guess a letter of the word: ").lower()
        if not guess.isalpha():
            print(f"{guess} is not a letter!")
            continue
        elif guess in NOT_VALID_LETTERS:
            print(f"{guess} is not a valid letter!")
            continue
        elif len(guess) > 1:
            print("Pick only one letter!")
            continue

        if guess in guessed_letters:
            print("Already guessed", guess)
            print("\n")
        elif guess in word:
            print("\n")
            print(f"Good job, the letter {guess} is in the word!")
            guessed_letters.append(guess)
            if hangman_counter >= 0:
                print(hangman[hangman_counter])
                print("\n")
        else:
            print(f"Unfortunately, {guess} is not in the word.")
            guessed_letters.append(guess)
            hangman_counter += 1
            tries -= 1
            print(hangman[hangman_counter])
            print("\n")
    if tries == 0:
        lose_round(word)


if __name__ == "__main__":
    init_game()
