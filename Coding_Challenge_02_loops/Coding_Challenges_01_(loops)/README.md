# Asks the user for a number `n` 
n = int(input("Enter a number n: "))
It use for input("Enter a number n: ") This prompts the user with the message `"Enter a number n:"` and waits for the user to type something.
int(...) This converts the input, which is typically a string, into an integer. If the user does not enter a valid number, it will raise a `ValueError`.

# Initialize a variable to store the sum
EX: total_sum = 0
The initial value must not affect the final result. Starting from `0` ensures that no unintended values are added.
Each iteration of the loop adds the current number (`num`) to the cumulative total stored in `total_sum`.

# Use a for loop to calculate the sum of numbers from 1 to n
This piece of Python code computes the sum of all integers from 1 to `n`and prints the result. Here's how it works step-by-step:
for num in range(1, n + 1):
    total_sum += num # Add the current number to the total sum
print(f"The sum of numbers from 1 to {n} is: {total_sum}")