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

    def to_json(self, attrs=None):
        """Retrive a dictionary representation of the
        class instance

        Args:
            attrs (list): list attributes to retrieve"""
        if type(attrs) is list:
            if all(type(item) is str for item in attrs):
                return {key: getattr(self, key)
                        for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """A public instance method that replaces all
        attributes of the Student instance

        Args:
            json (dict): the key and the value to replace
            the attribues with.
        """

        for key, value in json.items():
            setattr(self, key, value)
