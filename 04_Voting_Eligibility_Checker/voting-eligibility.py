# Asking for user input for age
age = int(input("Please enter your age: "))

# Checking if the age is 18 or older
if age >= 18:
    print("You are eligible to vote!")
elif age < 18:
    print("Sorry,you are not eligible to vote yet.")