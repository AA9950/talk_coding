# create two sets
EX: set_a = {1,2,3,4,5,}
set_b = {2,3,4}
to check if one set is a subset of another or if one set is a superset of another,
use the built-in methods in Python here's how you can do it with the sets set_a and set_b

# Check if `set_b` is a subset of `set_a` and print the result
EX: _subset = set_b.issubset(set_a)
print(f'{is_subset}')
set_b is considered a subset of set_a if all elements of set_b are also elements of set_a
in Python, you can use the issubset() method or the operator to check this

# Check if `set_a` is a superset of `set_b` and print the result
EX: is_superset = set_a.issuperset(set_b)
print(f'{is_superset}')
set_a is considered a superset of set_b if it contains all elements of set_b
in Python, you can use the issuperset() method or the operator to check this
