# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     18-mar-2025
# Updated:     18-Mar-2025
# -----------------------------------------------------------------------------


# Loop through numbers from 1 to 10
for i in range(1, 11):
    # Skip the iteration if the number is even
    if i % 2 == 0:
        continue
    # Print the number (this executes only for odd numbers)
    print(i)


