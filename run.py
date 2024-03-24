import random


def validate_guess():
    """
    Function that validates user input to ensure it is a single letter.
    Returns the validated letter or False if input is invalid.
    """
    user_input = input("Guess a letter: ").strip().upper()

    while True:
        try:

            if " " in user_input or not user_input.isalpha():
                raise ValueError(f"'{user_input}' is not a letter, try again.")
            elif len(user_input) != 1:
                raise ValueError("Enter a single letter.")
        except ValueError as e:
            print(f"Your entry is invalid: {e}, try again.")
            return False
        else:
            return user_input


guess = validate_guess()
