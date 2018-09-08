# Creating a guess game from scratch
#import the right module
# dat will get the job done

import random

# set a variable name to the import function

number = random.randint(1,15)

login_name = (input("What is your username: "))

guesses = [0]


while True:
    guess = (int(input("I am thinking of a number between 1 and 15, can you take a guess: ")))

    if guess < 1 or guess>15:
        print("Guess out of range!")

    if guess==number:
        print(f"Congratulation {login_name} \n It took you {len(guesses)} guesses")
        break

    if guess != number:
        print("Try again!")

        # guesses[-2] == 0
    # gusses == 0 guesses at index [-1]

    guesses.append(guess)

    if guesses:
        if abs(number-guess) < abs(number-guesses[-2]): # subsequent guess
            print('Very close')
        else:
            print("Too Far")


    else:
        if abs(number-guess) <= 10: # First guess
            print("Warm")
        else:
            print("cool")
