# Ask the user to input two numbers
EX: num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
the program starts by asking the user to input two numbers
the input() function is used to read the input from the user, and float() is used to convert the input strings to floating-point numbers

# # Store them in a tuple
EX: numbers = (num1, num2)
the two numbers entered by the user are stored in a tuple named numbers
tuples are a convenient way to group related data together
in this case, numbers will hold the two values as a single entity

# Swap their values without using a temporary variable
EX: num1, num2 = numbers[1], numbers[0]
the swapping of values is done using tuple unpacking 
instead of using a temporary variable, 
directly assign the values from the tuple to the variables num1 and num2 in a single line

# Print the swapped values
EX: print("Swapped values:")
print("First number:", num1)
print("Second number:", num2)
the program prints the swapped values of num1 and num2 using the print() function
this shows the user the results of the swap

