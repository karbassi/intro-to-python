# Homework 2 Answer

The [guess.py](guess.py) file is heavily documented. There are multiple ways to write this program, this is only one take on it.

## Examples

### Super Simple Win

```
What is the minimum number for my guess? 1
What is the maximum number for my guess? 1
Guess a number between 1 and 1: 1

 🎉 You won in 1 tries!
```

### Simple Win

```
What is the minimum number for my guess? 1
What is the maximum number for my guess? 2
Guess a number between 1 and 2: 1

 😢 Nope! You have 4 tries left.

Guess a number between 1 and 2: 2

 🎉 You won in 2 tries!
```

### Show user warnings

```
What is the minimum number for my guess? hello

 ⛔️ Please enter a number.

What is the minimum number for my guess? 1
What is the maximum number for my guess? hi

 ⛔️ Please enter a number.

What is the maximum number for my guess? 2
Guess a number between 1 and 2: salutations

 ⛔️ Please enter a number.

Guess a number between 1 and 2: 1

 🎉 You won in 1 tries!
```

### Lose

```
What is the minimum number for my guess? 1
What is the maximum number for my guess? 1000000000000
Guess a number between 1 and 1000000000000: 1

 😢 Nope! You have 4 tries left.

Guess a number between 1 and 1000000000000: 2

 😢 Nope! You have 3 tries left.

Guess a number between 1 and 1000000000000: 3

 😢 Nope! You have 2 tries left.

Guess a number between 1 and 1000000000000: 4

 😢 Nope! You have 1 tries left.

Guess a number between 1 and 1000000000000: 5

 😢 Nope! You have 0 tries left.


 😭 You lost. The number was 485100493025.
```
