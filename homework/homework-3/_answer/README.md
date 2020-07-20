# Homework 3 Answer

The [person.py](person.py) file is heavily documented. There are multiple ways to write this program, this is only one take on it.

## Examples

### No error

```python
jane = Person('Jane', '01/01/2000')

jane_age = jane.get_age()
print(jane_age) # 20

jane.set_weight(75)
jane.set_height(1.8)

jane_bmi = jane.get_bmi()
print(jane_bmi) # 23.15
```

### Making sure that `set_height()` and `set_weight()` convert strings to floats

```python
john = Person('John', '12/01/1973')

john_age = john.get_age()
print(john_age) # 47

john.set_weight('175.52')
john.set_height('2.1')

john_bmi = john.get_bmi()
print(john_bmi) # 39.8
```

### Making sure age is correct when the birthday just passed

```python
kelly = Person('Kelly', '23/07/1900')

kelly_age = kelly.get_age()
print(kelly_age) # 120

kelly.set_weight('210')
kelly.set_height('1.2')

kelly_bmi = kelly.get_bmi()
print(kelly_bmi) # 145.83
```

### Throwing errors if `name` is not a string

```python
bob = Person('', '01/01/2000') # throws an error since `name` requres 1 char
```

### Throwing errors if date conversion doesn't work

```python
bob = Person('bob', '45/07/1900') # throws an error trying to convert to a date
bob = Person('bob', 'july 15, 2020') # throws an error trying to convert to a date
bob = Person('bob', '') # throws an error trying to convert to a date
```
