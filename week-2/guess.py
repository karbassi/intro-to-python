#!/usr/bin/env python3

# import random
from random import randint

# program is going to pick a random number between 1 and 10
number = randint(1, 10)
# print(number)

# program is going to ask the player to guess the number
guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

# if they guess wrong, ask them again (forever)
while guess != number:
    print("Nope! Try again.")

    # program is going to ask the player to guess the number
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)

else:
    # if the player guesses correctly, display a message and quit
    print("You got it!")



