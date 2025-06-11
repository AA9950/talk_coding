# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     18-mar-2025
# Updated:     18-Mar-2025
# -----------------------------------------------------------------------------


# Prompt the user to enter a number
n = int(input("Enter a number n: "))
# Initialize a variable to store the sum
total_sum = 0
# Use a for loop to calculate the sum of numbers from 1 to n
for num in range(1, n + 1):
    total_sum += num # Add the current number to the total sum
print(f"The sum of numbers from 1 to {n} is: {total_sum}")




