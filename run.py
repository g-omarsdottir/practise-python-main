import random
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Words to guess in a tuple (immutable)
words = (
    "ant baboon badger bat bear beaver camel cat clam cobra cougar "
    "coyote crow deer dog donkey duck eagle ferret fox frog goat "
    "goose hawk lion lizard llama mole monkey moose mouse mule newt "
    "otter owl panda parrot pigeon python rabbit ram rat raven "
    "rhino salmon seal shark sheep skunk sloth snake spider "
    "stork swan tiger toad trout turkey turtle weasel whale wolf "
    "wombat zebra "
).split()

# r is raw string notation to solve syntax issues with hangman drawing.
hangman_drawing = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

guesses_left = len(hangman_drawing) - 1

print(guesses_left)
used_letters = []

def choose_play_game():
    """
    Function that welcomes the user to the game and asks if user wants to play.
    """
    print("Welcome to a game of Hangman!")
    print(hangman_drawing[0])
    print()

    while True:

        user_choice_play = input("Would you like to play? Your answer (y/n): ").strip().upper()
        if user_choice_play == "N":
            print("That's too bad, you don't want to play. Hope to see you soon!")
            return False
        elif user_choice_play == "Y":
            print("Good stuff, let's get your game on.")
            return choose_display_rules()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return False


def choose_display_rules():
    while True:
        user_choice_rules = input("Would you like to see the rules? (y/n) ").strip().upper()
        if " " in user_choice_rules or not user_choice_rules.isalpha():
            print("Invalid input. Please enter 'y' or 'n'.")
            return False
        elif user_choice_rules == "Y":
            print(
                """"The rules of the game are quite simple. 

                    You will get a set of blanks representing the number of letters in a word for an animal.
                    
                    Guess the word by entering one letter at a time and press enter.

                    You have 6 guesses. 
            
                    If you guess correctly, your letter(s) will appear on the blank(s).
            
                    If you fail, you have one less guess left and are one step closer to the gallows. 
    
                    So choose wisely!"""
            )
            return True
        else:
            print("You chose to dive right in without reading the rules. Alrighty then, game on!")
            return get_username()


def get_username():
    """
    Function to prompt the user to enter a username.
    Passes the username input for validation to the validate_username function.
    """
    while True:
        username_input = input("Choose your username: ").strip()
        if validate_username(username_input):
            return username_input


def validate_username(username_input):
    """
    Validate the username input to ensure it is between 1 and 10 characters.
    """
    if " " in username_input or not username_input.isalpha():
        print("Invalid username. Please use alphabetic characters and no spaces.")
        return False
    elif len(username_input) < 1 or len(username_input) > 10:
        print("Invalid username. Please use between 1 and 10 characters.")
        return False
    else:
        print(f"Welcome, {username_input}, let the games begin!")
        return True


def display_word_puzzle():
    """
    Function to generate a random word from tuple words.
    Convert word to uppercase for comparison with the user's guess.
    Generate blanks to indicate number of letters of word to guess.
    """
    word = random.choice(words).upper()
    blanks = "_ " * len(word)
    # New Attempt
    for _ in range(len(word)):
        new_blanks += f"{guess} "
#or
    for i in range(len(word)):
        if word[i] == guess:
            new_blanks += guess + " "
        else:
            new_blanks += guess + " "
    print(blanks)
    print(used_letters)
    print(hangman_drawing[guesses_left])


def get_user_guess():
    """
    Function to prompt the user to guess a letter.
    Convert input to uppercase for comparison with the word to guess.
    Passes the letter for validation to the validate_guess function.
    """
    while True:
        user_guess = input("Guess a letter: ").strip().upper()
        if validate_guess(user_guess):
            return user_guess


def validate_guess(user_guess):
    """
    Function that validates user input to ensure it is a single letter.
    Returns the validated letter or False if input is invalid.
    """
    if " " in user_guess or not user_guess.isalpha():
        print(f"'{user_guess}' is not a letter, try again.")
        return False
    elif len(user_guess) != 1:
        print("Enter a single letter.")
        return False
    # Add validation for used letters
    else:
        print(f"Let's see if {user_guess} works...")
        return compare_guess(user_guess)


def compare_guess(guess, word):
    """
    Function that compares user's guess with the word to guess and already used letters.
    Returns the correct guess or appends the wrong guess to used_letters list.
    """
    if guess in used_letters:
        print(f"You've already guessed {guess}. Try again.")
        return False
    elif guess not in word:
        used_letters.append(guess)
        guesses_left -= 1
    else:
        print(f"Great job, {guess} is correct!")
        return True
        # exchange letter for blanks


# global variables


def main():
    """
    Function to run all game functions
    """
    choose_play_game()
    choose_display_rules()
    
    username = get_username()
    display_word_puzzle()
    guess = get_user_guess()
    correct_guess = compare_guess()
    print(word)
    print(blanks)


main()
