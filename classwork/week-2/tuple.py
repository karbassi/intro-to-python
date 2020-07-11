#!/usr/bin/env python3

# Built-in data type: Sequence Types
# tuple (are immutable)

my_pets = (
    'dog',
    'cat',
)

your_pets = (
    'fish',
    'bobcat',
)

our_pets = my_pets + your_pets

# print( 'dog' in our_pets )
# print(my_pets)
# print(type(my_pets))
# print(my_pets[1])
# print(my_pets * 3)
# print(my_pets + your_pets)
# print(our_pets)

# ---
# looping
# print(type(groceries))
for pet in our_pets:
    print(pet)
