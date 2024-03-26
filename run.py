import random


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

# global variables
guesses_left = len(hangman_drawing) - 1
print(guesses_left)

used_letters = []

# Generate a random word from the tuple words.
# Convert word to uppercase for comparison with the user's guess.
word = random.choice(words).upper()

# Generate blanks to indicate number of letters of word to guess.
blanks = "_ " * len(word)


def choice_play_game():
    """
    Function that welcomes the user and prompts to make a choice.
    Choice is to continue to next step to play game.
    """
    print("Welcome to a game of Hangman!")
    print(hangman_drawing[0])
    print()

    while True:

        user_choice_play = input("Would you like to play? (y/n): ").strip().upper()
        if user_choice_play == "N":
            print("You choose not to play. See you later, alligator!")
            return False
        elif user_choice_play == "Y":
            print("You choose to play, glad to have you on board!")
            return True
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return False


def choice_display_rules():
    """
    Function that prompts the user to make a choice.
    Choice is to read the rules before playing game.
    """
    while True:
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
            return True
        elif user_choice_rules == "N":
            return choice_username()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return False


def choice_username():
    """
    Function to prompt the user to enter a username.
    Passes the username input for validation to the validate_username function.
    """
    while True:
        username = input("Choose your username: ").strip()
        if validate_username(username):
            return username


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
        return True


def display_word_puzzle():
    """
    Function that displays the word puzzle to the user.
    """
    print(word)  # To-do: delete
    print(blanks)
    print(used_letters)
    print(hangman_drawing[guesses_left])
    return get_guess()


def get_guess():
    """
    Function to prompt the user to guess a letter.
    Convert input to uppercase for comparison with the word to guess.
    Passes the letter for validation to the validate_guess function.
    """
    while True:
        guess = input("Guess a letter: ").strip().upper()
        if validate_guess(guess):
            return guess


def validate_guess(guess):
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
    # Add validation for used letters
    else:
        print(f"Let's see if {guess} works...")
        return compare_guess(guess)


def compare_guess(guess, word, guesses_left):
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
        return guesses_left
        # exchange letter for blanks


def main():
    """
    Function to run all game functions
    """
    choice_play_game()
    choice_display_rules()
    choice_username()
    display_word_puzzle()
    get_guess()
    compare_guess()


main()
