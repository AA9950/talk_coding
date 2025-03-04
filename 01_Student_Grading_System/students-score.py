# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     28-Feb-2025
# Updated:     28-Feb-2025
# -----------------------------------------------------------------------------


print("Welcome to my StudentGradingSystem")
myScore = (int(input("Enter your grade:")))
if myScore >= 90:
    print("Grade A")
    print("Congratulations, you are successful")
if 80 <= myScore <= 89:
    print("Grade B")
    print("Congratulations, you are successful")
else:
    print("The score is not between 80 and 89")
if 70 <= myScore <= 79:
    print("Grade C")
    print("Congratulations, you are successful")
else:
    print("The score is not between 70 and 79")
if 60 <= myScore <= 69:
    print("Grade D")
    print("Congratulations, you are successful")
else:
    print("The score is not between 60 and 69")
if myScore < 60:
    print("Grade F")
    print("Congratulations, you are successful")
if 0 <= myScore <= 49:
    print("Fail")
    print("Fail, try again")
print("Do you need any help?🤔")

