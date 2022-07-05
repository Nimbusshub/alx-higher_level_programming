#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """A class BaseGeometry"""

    def area(self):
        """raises an exception if not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(self.name))
