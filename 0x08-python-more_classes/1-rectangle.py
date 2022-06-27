#!/usr/bin/python3
""" class Rectangle that defines a rectangle."""


class Rectangle:
    """A class Rectangle with no attribute or instance.
    Instantiation with optional width and heigth.

    Args:
        width (int): the width of the class Rectangle.
        heigth (int): the height of the class Rectangle.
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width property getter: retrive the width of the class.

        Returns:
            int; the set instance attribute

        width.setter: set the width of the class.
        It also checks for TypeError and Value Error.

        Args:
            value (int): value to set the width to.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height property getter: retrive the height of the class.

        Returns:
            int: the set instance attribute

        height.setter: set the height of the class.
        It also checks for TypeError and Value Error.

        Args:
            value (int): value to set the width to.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
