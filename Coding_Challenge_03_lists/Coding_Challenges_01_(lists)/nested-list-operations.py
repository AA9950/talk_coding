# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Abdalle
# Created:     24-mar-2025
# Updated:     24-Mar-2025
# -----------------------------------------------------------------------------


# Create the students lists which contains the following data about three students
students = [
    ['Alice', 25, 'Physics'],
    ['Bob', 22, 'Chemistry'],
    ['Charlie', 24, 'Biology']
]

# Update Bob's age to 23 and his major to 'Mathematics'
students[1][1] = 23
students[1][2] = 'Mathematics'

# Print the updated students list
print("Updated students list:", students)

# Access and print the name of the student studying 'Biology'
for student in students:
    if student[2] == 'Biology':
        print("The student studying Biology is:", student[0])
        break
