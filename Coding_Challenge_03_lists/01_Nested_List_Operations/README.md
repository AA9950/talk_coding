# Create a list students which contains the following data about three students
EX:  [['Alice', 25, 'Physics'],['Bob', 22, 'Chemistry'],['Charlie', 24, 'Biology']]
Lists their name of the student, age of the student and major of the student

# Change Bob's age to 23 and his major to 'Mathematics'
EX: students[1][1] = 23
students[1][2] = 'Mathematics'
Changed the age of the student, and his major

# Print the updated students list
EX: print("Updated students list:", students)
Update the function list to new student list

# Access and print the name of the student who is studying 'Biology'
EX: for student in students:
    if student[2] == 'Biology':
        print("The student studying Biology is:", student[0])
        break
To find the student name who is studying 'Biology'
