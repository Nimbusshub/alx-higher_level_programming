#!/usr/bin/python3

"""A class Rectangle that inherits from class Base"""

from models.base import Base
import sys


class Rectangle(Base):
    """A class Rectangle that inherits from class Base.

    Instantiate with
    Args:
        width (int): width of the class Rectangle
        height (int): height of the class Rectangle
        x (int): x-axis of the class Rectangle
        y (int): y-axis of the class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.id = id
        super().__init__(self.id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property getter: retrieve the value of private
        instance attribute width

        width.setter: set the value of self.__width.
        Args:
            value (int): value to initialize self.__width with.

        Exceptions: Raises
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property getter: retrieve the value of private
        instance attribute height

        height.setter: set the value of self.__height.
        Args:
            value (int): value to initialize self.__height with.

        Exceptions: Raises
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property getter: retrieve the value of private
        instance attribute x

        x.setter: set the value of self.__x.
        Args:
            value (int): value to initialize self.__x with.

        Exceptions: Raises
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property getter: retrieve the value of private
            instance attribute y

        y.setter: set the value of self.__y.
        Args:
            value (int): value to initialize self.__y with.

        Exceptions: Raises
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of the class Rectangle

        Returns:
            the area of the class Rectangle
        """
        return self.__height * self.__width

    def display(self):
        """Method prints the rectangle instance with the character # to the stdout"""
        for i in range(self.__y):
            print("", file=sys.stdout)
        for i in range(self.__height):
            print(" " * self.__x, end="", file=sys.stdout)
            print("#" * self.__width, file=sys.stdout)

    def __str__(self):
        """Define the behaviour of the class Rectangle when called"""
        str_class = "[Rectangle]"
        str_id = " ({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.__x, self.__y)
        str_wh = "{}/{}".format(self.__width, self.__height)

        return str_class + str_id + str_xy + str_wh

    def update(self, *args):
        counter = 0
        for i in args:
            if isinstance(i, int):
                if counter == 0:
                    self.id = i
                elif counter == 1:
                    self.__width = i
                elif counter == 2:
                    self.__height = i
                elif counter == 3:
                    self.__x = i
                elif counter == 4:
                    self.__y = i
                counter += 1
