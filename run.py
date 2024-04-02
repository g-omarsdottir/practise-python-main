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

# global variables
allowed_wrong_guesses = 6

right_guesses = []

wrong_guesses = []

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
    print()
    print("\033[1;32;40m" + "—" * 39 + "\033[0m\n")
    print()


# Game functions


def return_to_menu():
    """
    Enables user to return to the game in case of unintended exit from game.
    """
    input("Press any key to return to the game menu.")
    clear_terminal()
    choice_play_game()


def choice_play_game():
    """
    Welcomes user and prompts to make a choice.
    Choice is to continue to next step to play game or exit.
    Validates user input.
    Resets game state when user plays again.
    """
    print("Welcome to a game of Hangman!")
    print(HANGMAN_DRAWING[6])
    print()
    right_guesses.clear()
    wrong_guesses.clear()
    global word_puzzle
    word_puzzle = ""
    global word
    word = random.choice(WORDS)

    user_choice_play = input("Would you like to play? (y/n): ").strip().upper()
    clear_terminal()
    if user_choice_play == "N":
        print("You chose not to play. See you later, alligator!")
        return_to_menu()
    elif user_choice_play == "Y":
        print("You chose to play, glad to have you on board!")
        choice_display_rules()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        user_choice_play


def choice_display_rules():
    """
    Prompts the user to make a choice.
    Choice is to read the rules before playing game.
    Validates user input.
    """
    user_choice_rules = (
        input("Would you like to read the rules? (y/n) ").strip().upper()
    )
    clear_terminal()
    if user_choice_rules == "Y":
        print(
            """
            Game rules:
            
            You will get a set of blanks representing
                the number of letters in a word.

            Guess the word by entering one letter at a time
                and press enter.

            You have 6 guesses.

            If you guess correctly,
                your letter(s) will appear on the blank(s).

            If you fail,
                you have one less guess left and
                are one step closer to the gallows.

            So choose wisely!
            """
        )
        choice_username()
    elif user_choice_rules == "N":
        choice_username()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        choice_display_rules()


def choice_username():
    """
    Function to prompt the user to enter a username.
    Passes the user input for validation to the validate_username function.
    """
    while True:
        username = input("Choose your username: ").strip()
        clear_terminal()
        if validate_username(username):
            return True


def validate_username(username):
    """
    Validates user input.
    Ensures it is between 1 and 10 characters.
    """
    if " " in username or not username.isalpha():
        print("Invalid username. Please use letters and no spaces.")
        return False
    elif len(username) < 1 or len(username) > 10:
        print("Invalid username. Please use between 1 and 10 characters.")
        return False
    else:
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
    used_letters = right_guesses + wrong_guesses
    print("Used letters: ", " ".join(used_letters))
    print()


def get_guess():
    """
    Prompts the user to guess a letter.
    Converts input to uppercase for comparison with the word to guess.
    Passes the letter for validation to the validate_guess function.
    """
    while True:
        guess = input("Guess a letter: ").strip().upper()
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
        visual_separator()
        print(f"'{guess}' is not a letter, try again.")
        visual_separator()
        return False
    elif len(guess) != 1:
        visual_separator()
        print("Enter a single letter.")
        visual_separator()
        return False
    else:
        print(f"Let's see if {guess} works...")
        return True


def compare_guess(guess):
    """
    Compares user's guess with the word to guess and already guessed letters.
    Displays user feedback for each user guess.
    Emphasises user feedback with visual separator.
    """
    if guess in right_guesses or guess in wrong_guesses:
        visual_separator()
        print(f"You've already guessed {guess}. Try again.")
        visual_separator()
    elif guess not in word:
        wrong_guesses.append(guess)
        visual_separator()
        print(f"Wrong guess, {guess} is not correct.")
        visual_separator()
    else:
        right_guesses.append(guess)
        visual_separator()
        print(f"Great job, {guess} is correct!")
        visual_separator()


def choice_play_again():
    """
    Prompts the user to make a choice.
    Choice is to play again or not.
    Validates user input.
    """
    user_choice_play_again = (
        input("Would you like to play again? (y/n) ").strip().upper()
    )
    clear_terminal()
    if user_choice_play_again == "N":
        print("You chose not to play again. See you in a while, crocodile!")
        return_to_menu()
    elif user_choice_play_again == "Y":
        print("You chose to play again, good stuff!")
        choice_play_game()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        user_choice_play_again


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
            display_game()
            print()
            print("Too bad, you lost.")
            print()
            print(f"The word to guess was: {word}")
            print()
            choice_play_again()
        elif set(right_guesses) == set(word):
            clear_terminal()
            print(HANGMAN_DRAWING[len(wrong_guesses)])
            print()
            print("Congratulations, you won!")
            print()
            print(f"The word to guess was: {word}")
            print()
            choice_play_again()


main()
