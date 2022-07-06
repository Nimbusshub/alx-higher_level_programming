#!/usr/bin/python3
"""Definition of a class Student"""


class Student:
    """A class Student with public instance attribute
    first_name, last_name and age

    The class is initiated with:

    Args:
        first_name (str): student's first name.
        last_name (str): student's last name.
        age (int): student's age.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrive a dictionary representation of the
        class instance"""
        return self.__dict__
