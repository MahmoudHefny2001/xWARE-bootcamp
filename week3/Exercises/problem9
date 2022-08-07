import random

n = random.randint(1, 100)

p = 0
counter = 0
nn = 0
while True:
    userInput = int(input("Please enter your guessing number: "))
    p = nn
    nn = userInput

    if p != nn:
        counter += 1

    if n == userInput:
        print("you guessed it right!")
        print("Number of multiple tries is: " + str(counter))
        break

    elif n > userInput:
        print("Your guessing is too small!")

    elif n < userInput:
        print("Your guessing is too high!")

