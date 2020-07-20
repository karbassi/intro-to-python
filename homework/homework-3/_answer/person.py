#!/usr/bin/env python3

from datetime import datetime


class Person:
    def __init__(self, name, birthday):
        # `name` is as string
        if not isinstance(name, str):
            raise TypeError("`name` needs to be a string.")

        # `name` of at least 1 character
        if len(name) < 1:
            raise Exception("`name` needs to be at least 1 character log.")

        # Save `name` to class
        self.name = name

        # `birthday` is as string
        if not isinstance(birthday, str):
            raise TypeError("`birthday` needs to be a string.")

        # `birthday` - as string formatted in day/month/year -
        # ex: `17/06/2000` or `17/6/2000` for July 17, 2020
        if len(birthday) < 8:
            raise Exception("`birthday` needs to be sent.")

        # If conversion doesn’t work, python will raise it's own exception.
        # We don't need to catch it since we want to raise it anyway
        self.birthday = datetime.strptime(birthday, "%d/%m/%Y")

    def set_weight(self, weight):
        """
        This function will save the `weight` to the class for later use.
        `weight` is required to float between `0.0` and `1000.0`.
        `weight` is in kilograms.
        """

        # Throw an error if not a `float`
        self.weight = float(weight)

        # Throw an error if not within the correct number range.
        if not (0 <= self.weight <= 1000):
            raise Exception("`weight` needs to be between 0 and 1000, inclusive.")

    def get_weight(self):
        """
        This function will return the class's `weight` as a float.
        """
        return float(self.weight)

    def set_height(self, height):
        """
        This function will save the `height` to the class for later use.
        `height` is required to float between `0.0` and `3.0`.
        `height` is in meters.
        """

        # Throw an error if not a `float`
        self.height = float(height)

        # Throw an error if not within the correct number range.
        if not (0 <= self.height <= 3):
            raise Exception("`height` needs to be between 0 and 3, inclusive.")

    def get_height(self):
        """
        This function will return the class's `height` as a float.
        """
        return float(self.height)

    def get_bmi(self):
        """
        Does the Body Mass Index calculations and returns a float _rounded_ to 2 decimals.
        """
        return round(self.weight / (self.height ** 2), 2)

    def get_age(self):
        """
        Returns the person's age in years (int), at the time of function call.
        """
        today = datetime.today()

        age = today.year - self.birthday.year

        # Check to see if the today's month and day is less than the birthday's
        # month and day. if it is, subtract one since they haven't had their
        # birthday yet
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1

        return age
