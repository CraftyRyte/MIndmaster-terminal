"""This program is a game called mind master"""

import random

# GLOBAL VARIABLES
COLORS = ["R", "G", "B", "W", "P", "Y"]


def starter():
    return """
              Welcome to Mindmaster
              Guess a 4 color code
              from [R, G, B, W, P, Y]
              
            """


def secret_code_generator():
    """
    Generates a secret code consisting of 4 random colors from a predefined list of COLORS.

    Returns:
    list: A list of 4 randomly selected colors from COLORS.
    """
    return random.sample(COLORS, 4)


def check_if_code_in_correct_pos(guess, code):
    """
    Check if the guessed code is in the correct position and/or incorrect position.

    Args:
    guess (str): A string representing the guessed code.
    code (str): A string representing the actual code.

    Returns:
    A tuple containing the number of correct positions and the number of incorrect positions.
    """
    correct_pos = 0
    incorrect_pos = 0
    for i in range(4):
        if (
            guess[i] == code[i]
        ):  # if the thing at i index of guess is equal to i index of code (means it is in correct pos)
            correct_pos += 1
        if (guess[i] in code) and (guess[i] != code[i]):  # to calculate incorrect pos
            incorrect_pos += 1

    return correct_pos, incorrect_pos


# function to get the user input
def take_guess():
    """
    This function takes user input for a guess and validates it.
    The guess should be a 4-color code, and each color should be one of the valid colors.
    Returns a list of the user's guess.
    """
    while True:  # To keep asking for guesses until a valid one is entered
        user_guess = input("Enter your guess: ").upper()
        user_guess_list = []
        for i in user_guess:
            user_guess_list.append(i)

        # check if the user input is valid
        if len(user_guess_list) != 4:
            print("Please enter exactly 4 colors.\n")
            continue
        if (
            user_guess_list[0] not in COLORS
            or user_guess_list[1] not in COLORS
            or user_guess_list[2] not in COLORS
            or user_guess_list[3] not in COLORS
        ):  # Just bruteforced it because did not know how to do it regularly
            print("Invalid color code.\n")
            continue

        break
    return user_guess_list


# This is the main function to run the game
def main():
    print(starter())
    code = secret_code_generator()
    no_of_guesses = 0
    isRunning = True

    while isRunning:
        no_of_guesses += 1
        if no_of_guesses > 6:
            print("Sorry, you ran out of your guesses")
            print("The correct code was,", code)
            break

        guess = take_guess()
        correct_pos, incorrect_pos = check_if_code_in_correct_pos(guess, code)

        if correct_pos == len(code):
            print(f"Congrats! You won in {no_of_guesses} guesses!")
            break
        else:
            print(
                f"In correct postion: {correct_pos} | In incorrect position: {incorrect_pos}\n"
            )


main()
