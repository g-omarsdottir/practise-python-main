import random
import os

# Constants

# Words to guess in a tuple (immutable)
WORDS = (
    "ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR"
    "COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT"
    "GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT"
    "OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN"
    "RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER"
    "STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF"
    "WOMBAT ZEBRA"
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
print("Allowed wrong guesses: ", allowed_wrong_guesses)

wrong_guesses = 0
print("Wrong guesses: ", wrong_guesses)
print(type(wrong_guesses))
guesses_left = allowed_wrong_guesses - wrong_guesses
print("Guesses left: ", guesses_left)

used_letters = []
print(used_letters)

# Generate a random word from the tuple words.
# Convert word to uppercase for comparison with the user's guess.
word = random.choice(WORDS)

# Generate dashes as "blanks" to indicate number of letters of word to guess.
word_puzzle = "_ " * len(word)


def clear_terminal():
    """
    Function to clear terminal screen for a better user experience.
    Imported built in os module to utilize OS-specific command to interact with operating system.
    """
    os.system("cls" if os.name == "nt" else "clear")


# Game functions


def return_to_menu():
    input("Press any key to return to the game menu.")
    clear_terminal()
    return choice_play_game()


def choice_play_game():
    """
    Function that welcomes the user and prompts to make a choice.
    Choice is to continue to next step to play game.
    """
    print("Welcome to a game of Hangman!")
    print(HANGMAN_DRAWING[6])
    print()
    user_choice_play = input("Would you like to play? (y/n): ").strip().upper()
    if user_choice_play == "N":
        print("You choose not to play. See you later, alligator!")
        return_to_menu()
    elif user_choice_play == "Y":
        print("You choose to play, glad to have you on board!")
        choice_display_rules()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        user_choice_play


def choice_display_rules():
    """
    Function that prompts the user to make a choice.
    Choice is to read the rules before playing game.
    """
    user_choice_rules = (
        input("Would you like to read the rules? (y/n) ").strip().upper()
    )
    if user_choice_rules == "Y":
        print(
            """
            You will get a set of blanks representing the number of letters in a word.
            
            Guess the word by entering one letter at a time and press enter.

            You have 6 guesses. 
                        
            If you guess correctly, your letter(s) will appear on the blank(s).
                        
            If you fail, you have one less guess left and are one step closer to the gallows. 
                
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
    Passes the username input for validation to the validate_username function.
    """
    while True:
        username = input("Choose your username: ").strip()
        if validate_username(username):
            return True


def validate_username(username):
    """
    Validate the username input to ensure it is between 1 and 10 characters.
    """
    if " " in username or not username.isalpha():
        print("Invalid username. Please use alphabetic characters and no spaces.")
        return False
    elif len(username) < 1 or len(username) > 10:
        print("Invalid username. Please use between 1 and 10 characters.")
        return False
    else:
        print(f"Welcome, {username}, let the games begin!")
        #get_guess()
        return True


def get_guess():
    """
    Function to prompt the user to guess a letter.
    Convert input to uppercase for comparison with the word to guess.
    Passes the letter for validation to the validate_guess function.
    """
    while True:
        win_loss_condition(used_letters, guesses_left, allowed_wrong_guesses, wrong_guesses, word_puzzle)
        guess = input("Guess a letter: ").strip().upper()
        if validate_guess(guess, used_letters):
            print("rendering function: get_guess")
        return guess


def validate_guess(guess, used_letters):
    """
    Function that validates user input to ensure it is a single letter.
    Returns the validated letter or False if input is invalid.
    """
    if " " in guess or not guess.isalpha():
        print(f"'{guess}' is not a letter, try again.")
        return False
    elif len(guess) != 1:
        print("Enter a single letter.")
        return False
    else:
        print(f"Let's see if {guess} works...")
        compare_guess(guess, word, word_puzzle, wrong_guesses, guesses_left, used_letters)
        return True


def compare_guess(guess, word, word_puzzle, wrong_guesses, guesses_left, used_letters):
    """
    Function that compares user's guess with the word to guess and already used letters.
    Returns the correct guess or appends the wrong guess to used_letters list.
    Updates count of wrong guesses.
    """
    while True: #guesses_left > 0: # move to win_loss_condition
        win_loss_condition(word_puzzle, allowed_wrong_guesses, wrong_guesses, guesses_left, used_letters)
        if guess in used_letters:
            print(f"You've already guessed {guess}. Try again.")
        elif guess not in word:
            #used_letters.append(guess)
            #wrong_guesses += 1
            #print(type(wrong_guesses))
            # updated_wrong_guesses = wrong_guesses + 1  # Store updated values
            #guesses_left - 1
            # updated_guesses_left = guesses_left - 1  # Store updated values
            print(f"Wrong guess, {guess} is not correct.")
            return used_letters, wrong_guesses, guesses_left
            # updated_wrong_guesses, updated_guesses_left,
        else:
            print(f"Great job, {guess} is correct!")
            #used_letters.append(guess)
            word_puzzle = [f"{letter}" if letter in word else "_" for letter in word]
            print("Word to guess: ", " ".join(word_puzzle))

            return word_puzzle, used_letters

def update_guess_status(guess, used_letters, wrong_guesses, guesses_left):
    # used_letters.append(guess)
    print("Used letters: ", " ".join(used_letters))
    wrong_guesses += 1
    print(type(wrong_guesses))
    guesses_left -= 1
    return used_letters, wrong_guesses, guesses_left


def win_loss_condition(used_letters, guesses_left, allowed_wrong_guesses, wrong_guesses, word_puzzle):
    """
    Function that displays the word puzzle to the user.
    Ends game when winning or losing conditions are met.
    """
    print(word)  # To-do: delete
    print(word_puzzle)
    print(used_letters)
    #print(HANGMAN_DRAWING[wrong_guesses])
    print("Rendering win_loss_condition: Allowed wrong guesses: ", allowed_wrong_guesses)
    print("Rendering win_loss_condition: Wrong guesses: ", wrong_guesses)
    print("Rendering win_loss_condition: Guesses left: ", guesses_left)
    if guesses_left > 0 and word_puzzle is word:
        print("Congratulations, you won!")
    elif guesses_left == 0 and "_" in word_puzzle:
        print("Too bad, you lost.")
        choice_play_again()


def choice_play_again():
    """
    Function that prompts the user to make a choice.
    Choice is to play again or not.
    """
    user_choice_play_again = input("Would you like to play again? (y/n) ").strip().upper()
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
    Function to run all game functions.
    """
    choice_play_game()
    guess = get_guess()
    #updated_wrong_guesses, updated_guesses_left, used_letters = compare_guess()
    # Update the original variables
    #wrong_guesses = updated_wrong_guesses
    #guesses_left = updated_guesses_left 
    compare_guess(guess, word, wrong_guesses, guesses_left, used_letters, word_puzzle)  # guess, word, wrong_guesses, guesses_left, used_letters
    update_guess_status(guess, used_letters, wrong_guesses, guesses_left)
    win_loss_condition(used_letters, guesses_left, allowed_wrong_guesses, wrong_guesses, word_puzzle)


# Your main() function does call compare_guess but doesn't do anything with the returned results.


main()
