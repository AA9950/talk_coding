# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     24-mar-2025
# Updated:     24-Mar-2025
# -----------------------------------------------------------------------------


# Create a list numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

# Create a list of even numbers using a list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# Create a list of squared numbers from the even numbers list using a list comprehension
squared_numbers = [num ** 2 for num in even_numbers]

# Print the even_numbers list
print("Even numbers:", even_numbers)

# Print the squared_numbers list
print("Squared even numbers:", squared_numbers)
