# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     8-Apr-2025
# Updated:     8-Apr-2025
# -----------------------------------------------------------------------------


# Create a set data
data = {10, 20, 30, 40, 50}

# Copy the set to data_copy
data_copy = data.copy()
print("Copy:", data_copy)

# Use .pop() to remove a random element
removed_element = data_copy.pop()
print("after pop:", data_copy)

# Use .clear() to empty the set
data_copy.clear()
print("after clear:", data_copy)
