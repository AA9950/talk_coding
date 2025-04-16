# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     18-mar-2025
# Updated:     18-Mar-2025
# -----------------------------------------------------------------------------


import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")
user_guess = 0
# Use a while loop to keep running until the guess is correct
while user_guess != random_number:
    # Ask the user for their guess
    user_guess = int(input("Guess the number (between 1 and 10): "))

    # Check if the guess is correct
    if user_guess == random_number:
        print("Correct! 🎉")
    else:
        print("Wrong, try again!")


