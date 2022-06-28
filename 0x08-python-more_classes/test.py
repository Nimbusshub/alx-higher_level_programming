#!/usr/bin/python3
Rectangle = __import__('rrr').Rectangle

my_square = Rectangle.square()
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
