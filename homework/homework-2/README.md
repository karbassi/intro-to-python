# Homework 2

Make a guess the number game where the program:

- asks the player for the minimum guess number
- asks the player for the maximum guess number
- checks the min and max numbers provided are correct; min has to be less than or equal to max.

Once they pick the min and max number, the game asks the player to guess the number in 5 tries. If they get it right within the 5 tries, they win. Display a message telling the player they won. If they don't get it right within the 5 tried, they lose. Display a message telling the player they lost and the number was X.

Extra 'points':

- the min, max, and guesses are required to be an int. If the player enters anything other than an int, the program displays a message and prompts the player to enter it again. _Hint_: Check out [try/except](https://www.google.com/search?q=python%20try%20except).

# Examples

```
What is the minimum number for my guess? 1
What is the maximum number for my guess? 5
Guess a number between 1 and 5: 3
Nope! you have 4 tries left.
Guess a number between 1 and 5: 2
You won in 2 tries!
```

```
What is the minimum number for my guess? 10
What is the maximum number for my guess? 2
Your minimum number needs to be less than your maximum number.
What is the minimum number for my guess? 2
What is the maximum number for my guess? 10
Guess a number between 2 and 10: 4
Nope! you have 4 tries left.
Guess a number between 2 and 10: 6
Nope! you have 3 tries left.
Guess a number between 2 and 10: 7
Nope! you have 2 tries left.
Guess a number between 2 and 10: 8
Nope! you have 1 tries left.
Guess a number between 2 and 10: 9
Nope! you have 0 tries left.
Guess a number between 2 and 10: 10
Nope! you have -1 tries left.
You lost. The number was 3.
```
