# Countdown from 10 to 1 with stop functionality
for num in range(10, 0, -1):
    print(num)
Use `range(start, stop, step)` when you need to iterate with a custom step size, especially negative steps for reverse loops.
`range(10, 0, -1)` is excellent for counting downward because it reduces the value of the loop variable with each iteration.

# Using the break for the num to cut
EX: user_input = input("Enter 'stop' to cancel or press Enter to continue: ").strip().lower()
    if user_input == 'stop':
        print("Countdown stopped by user.")
        break
For  this  one I use the input and add the print for the result 
after I use the break for the number to cut. then I use the stop comment for the user

# Use the else for the result
EX: else:
   print("Countdown completed.")
use the else for the ending the coding and I add the comment