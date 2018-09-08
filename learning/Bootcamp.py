import random

number = random.randint(1,10)
tries = 1


uname = input("Hello, What is your Username: ")



print("Hello", uname + ".", )


question = input("would you like to play a game? [Y/N] ")
if question == "n":
    print("oh...okay")

if question == "y":
    print("I'm thinking of a number between 1 & 10")
    guess = int(input("Have a guess: "))
    if guess > number:
        print("Guess lover...")
if guess < number:
    print("Guess higher")
while guess != number:
    tries += 1
    guess = int(input("Try again: "))
    if guess < number:
        print("Guess higher")
if guess == number:
    print("You're right! YOU WIN! The number was ", number, \
          "and it only", tries, "tries")


