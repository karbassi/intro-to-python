#!/usr/bin/env python3

"""
Make a guess the number game where the program:

- asks the player for the minimum guess number
- asks the player for the maximum guess number
- checks the min and max numbers provided are correct; min has to be less than
  or equal to max.

Once they pick the min and max number, the game asks the player to guess the
number in five tries. If they get it right within the five tries, they win.
Display a message telling the player they won. If they don't get it right
within the five tried, they lose. Display a message telling the player they
lost and the number was X.

Extra 'points':

- the min, max, and guesses are required to be an int. If the player enters
  anything other than an int, the program displays a message and prompts the
  player to enter it again.

  _Hint_: Check out `try/except`
          https://google.com/search?q=python%20try%20except
"""

from random import randint

# Loop until the user enters a `min` that is less than or equal to `max`
while True:

    # Loop until `guess_min` is a valid int
    while True:
        # Ask the user to enter a minimum number
        guess_min = input('What is the minimum number for my guess? ')

        # Try to convert user's input into an integer.
        try:
            guess_min = int(guess_min)
            # If conversion works, then `break` out of while loop
            break

        # If `int(guess_min)` throws an error,
        # then catch it...
        except ValueError:
            # ... and display a message
            print('\n ⛔️ Please enter a number.\n')

    # Loop until `guess_max` is a valid int
    while True:
        guess_max = input('What is the maximum number for my guess? ')

        # Try to convert user's input into an integer.
        try:
            guess_max = int(guess_max)

            # If conversion works, then `break` out of while loop
            break

        # If `int(guess_min)` throws an error,
        # then catch it...
        except ValueError:
            # ... and display a message
            print('\n ⛔️ Please enter a number.\n')

    # If `guess_min` less than or equal to `guess_max`, then break out of loop
    if guess_min <= guess_max:
        break

    # Otherwise, print an message to the user
    print('\n ⛔️ Your minimum number needs to be less than your maximum number.\n')


# Pick a random number between `guess_min` and `guess_max`
answer = randint(guess_min, guess_max)

# Create a variable that holds the number of guesses
guess_counter = 0
allowed_guesses = 5

# Loop until the user has guessed `allowed_guesses` times
while guess_counter < allowed_guesses:

    # Loop until `guess` is a valid int
    while True:
        # Ask the user to guess the number
        guess = input(f'Guess a number between {guess_min} and {guess_max}: ')

        # Make sure `guess` an int
        try:
            guess = int(guess)
            break

        # ... otherwise display message
        except ValueError:
            print('\n ⛔️ Please enter a number.\n')

    # Add 1 to `guess_counter`
    guess_counter += 1

    # If the user's guess matches the answer...
    if guess == answer:

        # ... then display a message
        print(f'\n 🎉 You won in {guess_counter} tries!\n')

        # ... and quit loop
        break

    # Otherwise, display a message with number of guesses left
    print(f'\n 😢 Nope! You have {allowed_guesses - guess_counter} tries left.\n')

else:

    # If they exit the loop because of it's conditional
    # check (guess_counter < 5), then the user lost and display a message
    print(f'\n 😭 You lost. The number was {answer}.\n')
