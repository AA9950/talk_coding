# Write a program that generates a random number between `1` and `10`
random_number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")
user_guess = 0
The `random.randint(1, 10)` function generates a random integer between `1` and `10` (inclusive).
This number is stored in the variable `random_number`.
You will need to import the `random` module in your program to use this function.

# Ask the user for their guess
user_guess = int(input("Guess the number (between 1 and 10): "))
It use to prompt the user to input their guess in a number guessing game. Here's a breakdown of how it works

# Check if the guess is correct
The given code uses an if-else statement to compare two values (`user_guess` and `random_number`) and provides feedback to the user based on the result:
    if user_guess == random_number:
        print("Correct! 🎉")
    else:
        print("Wrong, try again!")