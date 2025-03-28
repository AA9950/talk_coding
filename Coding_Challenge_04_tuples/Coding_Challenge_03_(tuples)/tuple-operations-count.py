# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     28-mar-2025
# Updated:     28-Mar-2025
# -----------------------------------------------------------------------------


# Create a tuple with repeated values
fruits = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Ask the user to enter a fruit name
user_fruit = input("Enter a fruit name: ")

# Count how many times the fruit appears in the tuple
count = fruits.count(user_fruit)

# Print the result
print(f"'{user_fruit}' appears {count} times in the tuple.")
