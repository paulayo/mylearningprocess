# For loop is used
# when you know the number
# of iteration required

fruits = ['Mango', 'Grapes', 'Apple']

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
