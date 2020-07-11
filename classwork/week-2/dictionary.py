#!/usr/bin/env python3

# Built-in data type:
# dictionary

# students = []

# student_a = {
#     'first_name': 'Jane',
#     'gender': 'female',
#     'age': 9,
# }

# student_b = {
#     'first_name': 'John',
#     'gender': 'male',
#     'age': 8,
# }

# students.append(student_a)
# students.append(student_b)

# print(students)



# ----

groceries = [
    {
        "name": "apples",
        "price": 1.99,
        "stock": 1,
    },
    {
        "name": "oranges",
        "price": 0.98,
        "stock": 1,
    },
    {
        "name": "pears",
        "price": 4.99,
        "stock": 1,
    },
    {
        "name": "kiwis",
        "price": 0.99,
        "stock": 1,
    },
    {
        "name": "oranges",
        "price": 0.99,
        "stock": 1,
    },
    {
        "name": "pears",
        "price": 0.99,
        "stock": 1,
    },
    {
        "name": "pears",
        "price": 0.99,
        "stock": 1,
    },
]

# ---
# looping
# print(type(groceries))
for item in groceries:
    print(f"{item['name']} at ${item['price']}")

# "apples at $1.99"
# "oranges at $0.98"
