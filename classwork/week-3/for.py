#!/usr/bin/env python3

# Syntax
# for <var> in <iterable>:
#     <statement(s)>

# # List
# primes = [2, 3, 5, 7]
# for prime in primes:
#     print(prime)

# # Tuple
# students = (
#     'Eddie',
#     'Ester',
#     'Jason',
#     'Kie',
#     'Minyi',
#     'Mithila',
#     'Scott',
#     'Shin',
#     'Stephanie',
# )

# for student in students:
#     print(student)

# # Set
# groceries = {
#     'apples',
#     'oranges',
#     'pears',
#     'kiwis',
# }

# for item in groceries:
#     print(item)

# # Dictionary
# jane = {
#     'first_name': 'Jane',
#     'gender': 'female',
#     'age': 9,
# }

# john = {
#     'first_name': 'John',
#     'gender': 'male',
#     'age': 9,
# }

# students = [
#     jane,
#     john,
# ]

# for student in students:
#     for key in student:
#         if key == 'first_name':
#             print(student[key])


# # Dictionary
# student = {
#     'first_name': 'Jane',
#     'gender': 'female',
#     'age': 9,
# }

# # student.values() returns a list
# # ['Jane', 'female', 9]

# for value in student.values():
#     print(value)


# Dictionary
# student = {
#     'first_name': 'Jane',
#     'gender': 'female',
#     'age': 9,
# }

# items() returns a key/value tuples in a list

# student.items() returns
# [
#   ('first_name', 'Jane'),
#   ('gender', 'female'),
#   ('age', 9)
# ]

# print(student.items())

# for key, value in student.items():
#     print(key, value)



# Range

# # range(stop)
# a = range(5)
# # print(a)

# # range(stop)
# for n in a:
#     print(n)

# for n in (0, 1, 2, 3, 4):
#     print(n)

# # range(stop)
# for n in range(5):
#     print(n)

# # range(start, stop)
# for n in range(5, 10):
#     print(n)


# This is a for loop going from 0 to 100, by 5s
# for n in range(0, 100, 5):
#     print(n)

# # from -10 to 10, by 2s
# for n in range(-10, 10, 2):
#     print(n)


for n in range(-5, 5):
    if n == 0:
        continue

    print(n)
