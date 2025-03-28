#  Create a tuple with five different elements
EX: element_tuple = (42, 3.14, 'Python', True, (1, 2, 3))
 Define a tuple named element_tuple that contains five different types of elements
tuples are defined using parentheses () and can hold a mix of data types

#  Print the entire tuple
EX: print(element_tuple)
Print the entire tuple using the print() function this will display all the elements contained in elements_tuple

# Access and print the third element
EX: print(element_tuple[2])
We access the third element of the tuple using indexing in Python, indexing starts at 0, so the third element is at index 2

# Extract the nested tuple and print its first element
EX: print(element_tuple[4][0])
The fifth element of element_tuple is another tuple (1, 2, 3), which we access using the index 4
We store this nested tuple in the variable element_tuple
To get the first element of this nested tuple, we again use indexing, accessing it with element_tuple[0]

