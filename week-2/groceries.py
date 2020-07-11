#!/usr/bin/env python3

# Built-in data type: Sequence Types
# list (mutable)

# groceries = list(
#     "apples",
#     "oranges",
# )

groceries = [
    "apples",
    "oranges",
    "pears",
    "kiwis",
    "oranges",
    "pears",
    "pears",
]

# print(groceries[3:6])

# example: groceries.count(x)
# Return the number of times x appears in the list (groceries).
# print(groceries.count("pears"))


# example: groceries.pop([index])
# Remove the item at the given position in the list, and return it.
# If no index is specified, a.pop() removes and returns the last item in the list.
# The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position.

# print(len(groceries)) # before: 6

# last_item = groceries.pop()
# print(last_item)

# print(len(groceries)) # after: 5
# item4 = groceries.pop(3)
# print(groceries)


# ---
# example: list.remove
# Remove the first item from the list whose value is equal to x.
# groceries.remove(x)

# groceries.remove("oranges")
# print(groceries)


# ---
# list.insert(index, item)

# insert at index 0
# groceries.insert(0, "grapes")

# insert at end
# groceries.insert(len(groceries), "mangos")
# print(groceries)


# ---

# print(groceries)

# item = input("What item do you want to add to groceries? ")
# groceries.append(item)

# print(len(groceries))

# print(groceries)


# ---
# list.sort()

# groceries.sort()
# print(groceries)


# # ---
# # looping
# # print(type(groceries))
# for item in groceries:
#     print(item)
