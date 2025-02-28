#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     28-Feb-2025
# Updated:     28-Feb-2025
#-----------------------------------------------------------------------------


print("Welcome to the TemperatureAdvice")
Temperature = (int(input("Enter the temperature: ")))
if Temperature < 10:
    print("It's cold outside.")
    print("Wear a jacket!")
if 10<= Temperature <=25:
        print("it's a nice day.")
        print("Wear short-sleeves!")
if Temperature > 25:
    print("It's hot outside.")
    print("Stay cool!")

