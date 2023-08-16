import random
from wordlist import word_list
from hangmanascii import hang_stages

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
        #print("Let's play!")
        start_game()
    elif roundstart == "n":
        print("What a pitty! Maybe you will change your mind and come back soon to save a man from hanging.")
    else:
        #raise ValueError("Answer must be 'n' or 'y'")
        print("Answer must be 'n' or 'y'")
        init_game()


def start_game():
    """
    Function for starting the actual game, including the previously defined funtions
    """
    word = random.choice(word_list)
    tries = 6
    correct_guesses = []
    incorrect_guesses = []

    #hangman_count = -1     #for future hangman display
    

    while tries > 0:
        output = ""
        for letter in word:
            if letter in correct_guesses:
                output += letter
            #elif letter = word:
            #   print("You guessed the word right!")
            else:
                output += "_ "
        if output == word:
            break 

        print("Guess the word: ", output)
        print(tries, " tries left")

        guess = input().lower()
        
        if guess in correct_guesses or guess in incorrect_guesses:
            print("Already guessed", guess)
        elif guess in word:
            print(f"Good job, the letter {guess} is in the word!")
            correct_guesses.append(guess)
        else:
            print(f"Unfortunately, {guess} is not in the word. Try again!")
            #hangman_count = hangman_count + 1
            tries = tries - 1
            incorrect_guesses.append(guess)
            #print(f"Hangmancount: {hangman_count}")
    if tries > 0:
        print(f"Splendid! You guessed the right word {word} and saved the man from being hanged!")
        nextround = input("Want to save some man's life again? y/n \n")
        if nextround == "y":
            start_game()
        elif nextround == "n":
            print("What a pitty! Maybe you will change your mind and come to play soon.")
    
    elif tries == 0:
        print(f"Game Over! The word was {word}")
        nextround = input("Want to play again? y/n \n")
        if nextround == "y":
            start_game()
        elif nextround == "n":
            print("What a pitty! Maybe you will change your mind and come back to save more men from hanging.")
    else:
        print("Sorry you guessed the wrong letter. Try again!")


def main():
    """
    Run all program functions
    """
    choose_word()

#main()

#init_game()

init_game()