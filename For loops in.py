# For loop is used
# when you know the number
# of iteration required

fruits = ['Mango', 'Grapes', 'Apple', 'Corn']

for friut in fruits:
    print("current fruit: ", friut)

print("Good bye")

num = int(input("Number: "))
factorial = 1

if num < 0:
    print("Must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
print(factorial)


# find the pythogarias by edureka['youtube']
# Nested loops example

from math import sqrt
n = int(input("Maximal Number?"))
for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
            print(a,b,c)

# using a for loop inside a while loop
# Bulk reservation:
# Name:
# Age:
# Sex:
# A train reservation ticket

travelling = input('yes or no: ')

while travelling == 'yes' or 'y':

    num = int(input("number of people travelling: "))

    for num in range(1, num+1):
        name = input("Name: ")

        age  =  input("Age: ")

        sex  = input("Male or Female: ")


        print(name)

        print(age)

        print(sex)

    travelling =  input("Oops! forgot someone: ")
