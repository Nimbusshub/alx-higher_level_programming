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

    def area(self):
        """Computes the area of the rectangle.

        Returns:
            int: area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Computes the perimeter of the rectangle.

        Returns:
            int: perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Defines the behavior of the objects of class Rectangle.

        Returns:
            str: print the rectangle with character "#"
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            if i != self.__height and i != 0:
                print()
            print("#" * self.__width, end="")

        return ""

    def __repr__(self):
        """ Produce string representation of the class Rectangle.

        Returns:
            str: representation of the class
        """
        container = "Rectangle(" + str(self.__width)
        container += ", " + str(self.__height) + ")"
        return (container)

    def __del__(self):
        print("Bye rectangle...")
