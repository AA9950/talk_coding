adding = 4 + 3
print(adding)

substraction = 8 - 9
print(substraction)

multiplacation = 4 * 32
print(multiplacation)

division = 50 / 5
print(division)

squared = 5**2
print(squared)

modulo = 15 % 4
print(modulo)

divisor = 15 // 4
print(divisor)
#New section
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)