import random


def welcome():
    """
    Function that welcomes the user to the game and explains the basic rules.
    """
    print("Welcome! Testing")

    print(
    """
    Welcome to a game of Hangman!
        
    You will get a set of blanks representing the number of letters in a word.
    Guess the word by entering one letter at a time and press enter.
            
    If you guess correctly, your letter(s) will appear on the blank(s).
            
    With each incorrect guess, one element will be added to the stick figure
    on the gallows, so choose wisely. 
            
    After 6 incorrect guesses, the stick figure is complete and it’s game over.
            
    Let the games begin!
            
    """
    )


def get_username():
    """
    Function that prompts the user to enter a username.
    """
    while True:
        username_input = (
            input("Choose your username: ").strip().upper()
        )
        if validate_username(username_input):
            return username_input


def validate_username(username_input):
    """
    Function that validates the username input to ensure it is between 1 and 10 characters.
    """
    if " " in username_input or not username_input.isalpha():
        print(f"'{username_input}' is not a valid username. \n Try again and use up to 10 alphabetic characters.")
    else:
        return username_input


def get_user_input():
    """
    Function that prompts the user to guess a letter and passes it to the validate_guess function.
    """
    while True:
        user_input = input("Guess a letter: ").strip().upper()
        if validate_guess(user_input):
            return user_input


def validate_guess(user_input):
    """
    Function that validates user input to ensure it is a single letter.
    Returns the validated letter or False if input is invalid.
    """
    if " " in user_input or not user_input.isalpha():
        print(f"'{user_input}' is not a letter, try again.")
        return False
    elif len(user_input) != 1:
        print("Enter a single letter.")
        return False
    # Add validation for used letters
    else:
        return user_input


welcome()
username = get_username()
guess = get_user_input()
used_letters = []
