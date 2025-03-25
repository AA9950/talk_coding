#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     28-Feb-2025
# Updated:     28-Feb-2025
#-----------------------------------------------------------------------------




print("Welcome to the Day of the Week Activity Recommender!")
day = input("Enter the current day of the week: ")

if day == "monday":
    print("Start your week with a workout!")
elif day == "tuesday":
    print("It's a great day to read a book!")
elif day == "wednesday":
    print("Mid-week movie night!")
elif day == "thursday":
    print("Try a new recipe!")
elif day == "friday":
    print("Relax and enjoy the weekend!")
elif day == "saturday":
    print("Go for a hike!")
elif day == "sunday":
    print("Prepare for the week ahead with some self-care.")
else:
    print("Invalid day. Please check your input.")




