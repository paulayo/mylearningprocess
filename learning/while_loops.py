# print the number between 0 to 8 excluding 9
count = 0

while count < 9:
    print("Number:", count)
    count = count + 1

print("Good bye")

# a guess game for learning while loop by edureka
import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")
