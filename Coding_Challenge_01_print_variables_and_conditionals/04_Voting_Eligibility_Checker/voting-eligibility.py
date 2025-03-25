#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     28-Feb-2025
# Updated:     28-Feb-2025
#-----------------------------------------------------------------------------


# Asking for user input for age
age = int(input("Please enter your age: "))

# Checking if the age is 18 or older
if age >= 18:
    print("You are eligible to vote!")
elif age < 18:
    print("Sorry,you are not eligible to vote yet.")