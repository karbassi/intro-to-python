#!/usr/bin/env python3

# CLASSES!

# Syntax for creating a function
#
# class <class_name>(<parent>):
#     <statement(s)>

# Syntax for calling a function
# <variable> = <class_name>()


class Dog:
    """A simple dog class"""

    # variables
    years_to_human = 7

    def __init__(self, name, gender, breed, color, age):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.color = color
        self.age = age

    def speak(self, sound='woof'):
        print(f'{self.name} says {sound}!')

    def set_sound(self, sound):
        self.sound = sound

    def get_sound(self):
        return self.sound

    def get_human_age(self):
        return self.age * self.years_to_human


charlie = Dog(name='Charlie', gender='male', breed='westie', color='white', age=13)

# print(charlie.name)

# maisie is 5 months
maisie = Dog(age=(5/12), name='Maisie', breed='scottie', gender='female', color='black')

print(maisie.get_human_age())

# # print(maisie.name)
# # print(maisie.color)
# # print(maisie.gender)
# # print(maisie.age)


# # maisie.speak('yip yip yip')
# # charlie.speak()


# maisie.set_sound('yip yip yip yip bork')
# maisie.speak()
