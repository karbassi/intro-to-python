#!/usr/bin/env python3

import unittest
from datetime import datetime

from person import Person


class TestPerson(unittest.TestCase):
    def test_init_no_params(self):
        self.assertRaises(Exception, Person)

    def test_init_no_name(self):
        self.assertRaises(Exception, Person, birthday="01/01/2000")

    def test_init_no_date(self):
        self.assertRaises(Exception, Person, name="Jane")

    def test_init_date_not_string(self):
        """
        Tests `birthday` to be %d/%m/%Y
        """
        today = datetime.today()
        self.assertRaises(Exception, Person, name="Jane", birthday=today)

    def test_class_type(self):
        jane = Person("Jane", "01/01/2000")
        self.assertIsInstance(jane, Person)

    def test_get_age(self):
        jane = Person("Jane", "01/01/2000")
        result = jane.get_age()
        self.assertEqual(result, 20)

    def test_set_weight_int(self):
        """Test to make sure that weight can be an int"""
        jane = Person("Jane", "01/01/2000")
        self.assertIsNone(jane.set_weight(75))

    def test_set_weight_float(self):
        jane = Person("Jane", "01/01/2000")
        self.assertIsNone(jane.set_weight(175.52))

    def test_set_weight_under_min(self):
        jane = Person("Jane", "01/01/2000")
        self.assertRaises(Exception, jane.set_weight, -1)

    def test_set_weight_over_max(self):
        jane = Person("Jane", "01/01/2000")
        self.assertRaises(Exception, jane.set_weight, 1001)

    def test_set_weight_not_number(self):
        jane = Person("Jane", "01/01/2000")
        self.assertRaises(Exception, jane.set_weight, "hello")

    def test_get_weight(self):
        jane = Person("Jane", "01/01/2000")
        jane.set_weight(100)
        result = jane.get_weight()
        self.assertEqual(result, 100)

    def test_set_height_int(self):
        jane = Person("Jane", "01/01/2000")
        self.assertIsNone(jane.set_height(2))

    def test_set_height_float(self):
        jane = Person("Jane", "01/01/2000")
        self.assertIsNone(jane.set_height(2.5))

    def test_set_height_under_min(self):
        jane = Person("Jane", "01/01/2000")
        self.assertRaises(Exception, jane.set_height, -1)

    def test_set_height_over_max(self):
        jane = Person("Jane", "01/01/2000")
        self.assertRaises(Exception, jane.set_height, 3.1)

    def test_set_height_not_number(self):
        jane = Person("Jane", "01/01/2000")
        self.assertRaises(Exception, jane.set_height, "hello")

    def test_get_height(self):
        jane = Person("Jane", "01/01/2000")
        jane.set_height(2.5)
        result = jane.get_height()
        self.assertEqual(result, 2.5)

    def test_get_bmi(self):
        jane = Person("Jane", "01/01/2000")
        jane.set_weight(75)
        jane.set_height(1.8)
        result = jane.get_bmi()
        self.assertEqual(result, 23.15)


class TestPersonExtras(unittest.TestCase):
    def test_init_wrong_date_short(self):
        """
        Tests `birthday` to be %d/%m/%Y
        """
        self.assertRaises(Exception, Person, name="Jane", birthday="12/25/2000")

    def test_init_wrong_date_long(self):
        """
        Tests `birthday` to be %d/%m/%Y
        """
        self.assertRaises(Exception, Person, name="Jane", birthday="January 15, 2000")

    def test_age_birthday_is_today(self):
        today = datetime.today()
        last_year = datetime(today.year - 1, today.month, today.day)
        last_year_formatted = last_year.strftime("%d/%m/%Y")

        jane = Person("Jane", last_year_formatted)
        result = jane.get_age()

        self.assertEqual(result, 1)

    def test_age_birthday_is_tomorrow(self):
        today = datetime.today()
        last_year = datetime(today.year - 10, today.month, today.day + 1)
        last_year_formatted = last_year.strftime("%d/%m/%Y")

        jane = Person("Jane", last_year_formatted)
        result = jane.get_age()

        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
