# Create a tuple with repeated values
EX: fruits = ("apple", "banana", "apple", "cherry", "banana", "apple")
define a tuple named fruits that contains several fruit names, including repeated values
is defined using parentheses () and contains the strings

# Ask the user to enter a fruit name
EX: user_fruit = input("Enter a fruit name: ")
the program prompts the user to enter a fruit name using the input() function

# Count how many times the fruit appears in the tuple
EX: count = fruits.count(user_fruit)
the program uses the count() method of the tuple to determine 
how many times the user-provided fruit name appears in the fruits tuple

# Print the result
EX: print(f"'{user_fruit}' appears {count} times in the tuple.")
the program prints the result using an f-string, which allows for easy formatting of the output
it displays how many times the specified fruit appears in the tuple
