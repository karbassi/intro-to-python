#!/usr/bin/env python3

# FUNCTIONS

# Syntax for creating a function
# def <function_name>([<parameters>]):
#     <statement(s)>

# Syntax for calling a function
# <function_name>([<arguments>])




# def say_hello(name):
#     print(f'Hello {name}!')

# say_hello("Ali")
# say_hello("Jason")
# say_hello("Eddie")
# say_hello("Shin")
# say_hello("Esther")
# say_hello("Scott")
# say_hello("Kie")
# say_hello("Mithila")
# say_hello("Minya")
# say_hello("Stephanie")


# def add(a, b):
#     sum = a + b
#     return sum

# x = add(1, 2)
# print(x)

# x = add(276324, 923745)
# print(x)

# divide
# def 除(あ, い):
#     う = あ / い
#     return う

# う = 除(10, 2)
# print(う)

# def divide(x, y):
#     if y == 0:
#         print('You cannot divide by zero.')
#         return

#     return x / y

# a = divide(10, 2)
# print(a)

# b = divide(1, 0)
# print(b)


# def multiple(a, b):
#     """This multiples `a` and `b` and returns the product"""
#     return a * b

# a = multiple(10, 100)




# def animal_speaks(animal, sound):
#     print(f'The {animal} says {sound}.')

# animal_speaks('cat', 'meow')

# animal_speaks('dog', 'woof')
# animal_speaks(animal='dog', sound='woof')
# animal_speaks(sound='woof', animal='dog')


# def animal_speaks(animal, sound='nothing'):
#     print(f'The {animal} says {sound}.')


# animal_speaks(animal='dog')
# animal_speaks('bulldog', 'woof')



# def average(a, b, c):
#     return (a + b + c) / 3

# x = average(1, 2, 3)
# print(x)

# x = average(28378934, 324897234, 32198732137)
# print(x)

# Argument Tuple Packing

# def average(numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total / len(numbers)

# a = average([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(a)

# def average(*number):
#     return sum(number) / len(number)

# x = average(1, 2, 3, 4, 5, 6, 92138, 2138923, -1238923, -12381237)
# print(x)
