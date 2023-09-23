""""This program is a game called mind master"""

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
    r1 = random.randint(0, 3)
    r2 = random.randint(0, 3)
    r3 = random.randint(0, 3)
    r4 = random.randint(0, 3)
    code = [COLORS[r1], COLORS[r2], COLORS[r3], COLORS[r4]]
    return code


def check_if_code_in_correct_pos(guess, code):
    """
    Check if the guessed code is in the correct position and/or incorrect position.

    Args:
    guess (str): A string representing the guessed code.
    code (str): A string representing the actual code.

    Returns:
    A tuple containing the number of correct positions and the number of incorrect positions.
    """
    code_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    for i in range(4):
        if guess[i] == code[i]:
            correct_pos += 1
        else:
            code_counts[code[i]] = code_counts.get(code[i], 0) + 1

    for i in range(4):
        if guess[i] != code[i] and guess[i] in code_counts and code_counts[guess[i]] > 0:
            incorrect_pos += 1
            code_counts[guess[i]] -= 1

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

        # check if the user input is valid
        if len(user_guess) != 4 or not all(c in COLORS for c in user_guess):
            print("Invalid color code.\n")
            continue

        break
    return user_guess


# This is the main function to run the game
def main():
    print(starter())
    code = secret_code_generator()
    print(code)
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
