#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """A class BaseGeometry"""

    def area(self):
        """raises an exception if not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method that validates value
        Args:
            name (str): name of the object
            value (int): value to initialise the base with
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
