import random
import os

# Constants

# Words to guess in a tuple (immutable)
WORDS = (
    "ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR "
    "COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT "
    "GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT "
    "OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN "
    "RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER "
    "STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF "
    "WOMBAT ZEBRA "
).split()

# r is raw string notation to solve syntax issues with hangman drawing.
HANGMAN_DRAWING = [
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
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

# global variables
allowed_wrong_guesses = 6

right_guesses = []

wrong_guesses = []

guesses_list = []

# Generate a random word from the tuple words.
# Convert word to uppercase for comparison with the user's guess.
word = random.choice(WORDS)

# Generate dashes to indicate number of letters of word to guess.
word_puzzle = "_ " * len(word)


# Functions


def clear_terminal():
    """
    Clears terminal screen for a better user experience.
    Imported built in os module to utilize OS-specific
        command to interact with operating system.
    """
    os.system("cls" if os.name == "nt" else "clear")


def visual_separator():
    """
    Prints a decorative line for visual separation for user feedback.
    """
    print("\033[1;32;40m" + "—" * 39 + "\033[0m\n")


# Game functions


def return_to_menu():
    """
    Enables user to return to the game in case of unintended exit from game.
    """
    print()
    input("Press enter to return to the game menu.\n")
    clear_terminal()
    choice_play_game()


def choice_play_game():
    """
    Welcomes user and prompts to make a choice.
    Choice is to continue to next step to play game or exit.
    Validates user input.
    Resets game state when user plays again.
    """
    print()
    print("Welcome to a game of Hangman!")
    print(HANGMAN_DRAWING[6])
    print()
    right_guesses.clear()
    wrong_guesses.clear()
    global word_puzzle
    word_puzzle = ""
    global word
    word = random.choice(WORDS)

    user_choice_play = input("Would you like to play? (y/n):\n").strip().upper()
    clear_terminal()
    if user_choice_play == "N":
        print()
        print("You chose not to play. See you later, alligator!")
        return_to_menu()
    elif user_choice_play == "Y":
        print()
        print("You chose to play, glad to have you on board!")
        choice_display_rules()
    else:
        print()
        print("Invalid input. Please enter 'y' or 'n'.")
        choice_play_game()


def choice_display_rules():
    """
    Prompts the user to make a choice.
    Choice is to read the rules before playing game.
    Validates user input.
    """
    print()
    user_choice_rules = (
        input("Would you like to read the rules? (y/n)\n").strip().upper()
    )
    clear_terminal()
    if user_choice_rules == "Y":
        print(
            """
Game rules:

You will get a word puzzle as a set of dashes,
representing the number of letters in the word to guess.

Guess the word by entering one letter at a time
and press enter.

You have 6 guesses.

If you guess correctly,
your letter(s) will appear in the word puzzle.

If you fail,
you have one less guess left and
you are one step closer to the gallows.

Good luck!"""
        )
        choice_username()
    elif user_choice_rules == "N":
        choice_username()
    else:
        print()
        print("Invalid input. Please enter 'y' or 'n'.")
        choice_display_rules()


def choice_username():
    """
    Function to prompt the user to enter a username.
    Passes the user input for validation to the validate_username function.
    """
    while True:
        print()
        username = input("Choose your username:\n").strip()
        clear_terminal()
        if validate_username(username):
            return True


def validate_username(username):
    """
    Validates user input.
    Ensures it is between 1 and 10 characters.
    """
    if " " in username or not username.isalpha():
        print()
        print("Invalid username. Please use letters and no spaces.")
        return False
    elif len(username) < 1 or len(username) > 10:
        print()
        print("Invalid username. Please use between 1 and 10 characters.")
        return False
    else:
        print()
        print(f"Welcome, {username}, let the games begin!")
        return True


def display_game():
    """
    Displays the game to the user.
    Updates the displayed word_puzzle.
    Updates the list of used letters.
    """
    print(HANGMAN_DRAWING[len(wrong_guesses)])
    guesses_left = allowed_wrong_guesses - len(wrong_guesses)
    print("Guesses left: ", guesses_left)
    print()
    word_puzzle = [letter if letter in right_guesses else "_" for letter in word]
    print("The Word to guess is: ", " ".join(word_puzzle))
    print()
    print("Used letters: ", " ".join(guesses_list))
    print()


def get_guess():
    """
    Prompts the user to guess a letter.
    Converts input to uppercase for comparison with the word to guess.
    Passes the letter for validation to the validate_guess function.
    """
    while True:
        guess = input("Guess a letter:\n").strip().upper()
        clear_terminal()
        is_guess_valid = validate_guess(guess)
        if is_guess_valid is not False:
            return guess
        else:
            display_game()


def validate_guess(guess):
    """
    Validates user input to ensure it is a single letter.
    Returns the validated letter or False if input is invalid.
    Emphasises user feedback for invalid input with visual separator.
    """
    if " " in guess or not guess.isalpha():
        print()
        print(f"'{guess}' is not a letter, try again.")
        visual_separator()
        return False
    elif len(guess) != 1:
        print()
        print("Enter a single letter.")
        visual_separator()
        return False
    else:
        return True


def compare_guess(guess):
    """
    Compares user's guess with the word to guess and already guessed letters.
    Displays user feedback for each user guess.
    Emphasises user feedback with visual separator.
    """
    if guess in right_guesses or guess in wrong_guesses:
        print()
        print(f"You've already guessed {guess}. Try again.")
        visual_separator()
    elif guess not in word:
        append_guesses_list(guess, False)
        print()
        print(f"Wrong guess, {guess} is not correct.")
        visual_separator()
    else:
        append_guesses_list(guess, True)
        print()
        print(f"Great job, {guess} is correct!")
        visual_separator()


def append_guesses_list(guess, correct):
    guesses_list.append(guess)
    if correct:
        right_guesses.append(guess)
    else:
        wrong_guesses.append(guess)


def choice_play_again():
    """
    Prompts the user to make a choice.
    Choice is to play again or not.
    Validates user input.
    """
    user_choice_play_again = (
        input("Would you like to play again? (y/n)\n").strip().upper()
    )
    clear_terminal()
    if user_choice_play_again == "N":
        print()
        print("You chose not to play again. See you in a while, crocodile!")
        return_to_menu()
    elif user_choice_play_again == "Y":
        print()
        print("Great, let's restart the game.")
        choice_play_game()
    else:
        print()
        print("Invalid input. Please enter 'y' or 'n'.")
        print()
        choice_play_again()


def main():
    """
    Run all game functions.
    Handles win or loss condition to end game.
    """
    choice_play_game()
    while True:
        display_game()
        guess = get_guess()
        compare_guess(guess)
        if len(wrong_guesses) == allowed_wrong_guesses:
            clear_terminal()
            display_game()
            visual_separator()
            print("Too bad, you lost.")
            print()
            print(f"The word to guess was: {word}")
            print()
            visual_separator()
            choice_play_again()
        elif set(right_guesses) == set(word):
            clear_terminal()
            display_game()
            visual_separator()
            print("Congratulations, you won!")
            print()
            visual_separator()
            choice_play_again()


main()
