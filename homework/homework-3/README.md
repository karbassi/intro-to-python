# Homework 3

Class Video: <https://youtu.be/rG3jnPlHsOA>

**Due:** July 24, 2020 at 02:00 PM CT

# Overview

**Note:** To keep things simple, all units are in metric.

Make a `person.py` file with a `Person` class. The `Person` class should take, via the `__init__` function:

- `name` - as string of at least 1 character - ex: `John`, `Jane`, `Kelly`
- `birthday` - as string formatted in day/month/year - ex: `17/6/2000` or `17/06/2000` for July 17, 2020

# Functions

The `Person` class should have the following functions:

## `set_weight(weight)`

This function will save the `weight` to the class for later use. `weight` is required to able to convert to a float between `0.0` and `1000.0`. `weight` is in kilograms.

Throw an error if `weight` cannot be converted to a `float` or not within the correct number range.

## `get_weight()`

This function will return the class's `weight` as a float.

## `set_height(height)`

This function will save the `height` to the class for later use. `height` is required to able to convert to a float between `0.0` and `3.0`. `height` is in meters.

Throw an error if `height` cannot be converted to a `float` or not within the correct number range.

## `get_height()`

This function will return the class's `height` as a float.

## `get_bmi()`

Does the [Body Mass Index](https://en.wikipedia.org/wiki/Body_mass_index) (BMI) calculations and returns a float _rounded_ to 2 decimals.

## `get_age()`

Returns the person's age in years (int), at the time of function call. You'll need to use the python's `datetime` library.

# Examples

The following calls should work, but I will test with much more.

```python
jane = Person('Jane', '01/01/2000')

jane_age = jane.get_age()
print(jane_age) # 20

jane.set_weight(75)
jane.set_height(1.8)

jane_bmi = jane.get_bmi()
print(jane_bmi) # 23.15
```

```python
john = Person('John', '12/01/1973')

john_age = john.get_age()
print(john_age) # 47

john.set_weight(175.52)
john.set_height(2.1)

john_bmi = john.get_bmi()
print(john_bmi) # 39.8
```

```python
kelly = Person('Kelly', '22/07/1900')

kelly_age = kelly.get_age()
print(kelly_age) # 119 or 120

kelly.set_weight('210')
kelly.set_height('1.2')

kelly_bmi = kelly.get_bmi()
print(kelly_bmi) # 145.83
```

# Tips

- [Raising an Exception](https://realpython.com/python-exceptions/#raising-an-exception)
- [`isinstance()`](https://www.w3schools.com/python/ref_func_isinstance.asp)
- [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)
- [Convert Python String to DateTime Object](https://www.tutorialkart.com/python/python-datetime/python-string-to-datetime/)
- [BMI Formula](https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php)
- [round](https://docs.python.org/3/library/functions.html#round)
