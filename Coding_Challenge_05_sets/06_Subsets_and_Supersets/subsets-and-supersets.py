# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     8-Apr-2025
# Updated:     8-Apr-2025
# -----------------------------------------------------------------------------


# Create two sets
set_a = {1,2,3,4,5,}
set_b = {2,3,4}

# Check if `set_b` is a subset of `set_a` and print the result
is_subset = set_b.issubset(set_a)
print(f'{is_subset}')

# Check if `set_a` is a superset of `set_b` and print the result
is_superset = set_a.issuperset(set_b)
print(f'{is_superset}')