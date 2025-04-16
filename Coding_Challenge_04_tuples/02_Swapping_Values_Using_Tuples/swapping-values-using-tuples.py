# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     28-mar-2025
# Updated:     28-Mar-2025
# -----------------------------------------------------------------------------


# Ask the user to input two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Store them in a tuple
numbers = (num1, num2)

#  Swap their values without using a temporary variable
num1, num2 = numbers[1], numbers[0]

# Print the swapped values
print("Swapped values:")
print("First number:", num1)
print("Second number:", num2)
