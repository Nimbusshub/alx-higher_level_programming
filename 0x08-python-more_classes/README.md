# Python - More Classes and Objects

Python is an Object Oriented Programming Language (OOP). Classes and Objects are the two main aspect of OOP. A **class** creates a new type while **objects** are instances of the class.

### Classes

The simplest definition of class in python is shown in the example below (save as `simple_class.py`):

```bash
#!/usr/bin/python3
class Rectangle:
"""An empty class Rectangle that defines a rectangle"""
    pass  # An empty block

Object1 = Rectangle()
print(Object1)

```

#### Output:

```
$ ./simple_class.py
<class '__main__.Rectangle'>

```

## Files

| Filename             | Description                                                                         |
| -------------------- | ----------------------------------------------------------------------------------- |
| [`0-rectangle.py`]() | Empty class `Rectangle` that defines a rectangle                                    |
| [`1-rectangle.py`]() | Class `Rectangle` that defines a rectangle by its `width` and `height`              |
| [`2-rectangle.py`]() | Class `Rectangle` that has `area` and `permiter` methods                            |
| [`3-rectangle.py`]() | Class `Rectangle` that counts with a string representation                          |
| [`4-rectangle.py`]() | Class `Rectangle` that count with an official representation                        |
| [`5-rectangle.py`]() | Class `Rectangle` that prints a message when an instance is deleted                 |
| [`6-rectangle.py`]() | Class `Rectangle` with a public class attribute that counts the number of instances |
| [`7-rectangle.py`]() | Class `Rectangle` with a public class attribute to print a specific symbol          |
| [`8-rectangle.py`]() | Class `Rectangle` with a method to compare instance's size                          |
| [`9-rectangle.py`]() | Class `Rectangle` with a class method that returns a new instance as a square       |
| [`101-nqueens.py`]() | `Backtracking` algorithm that solves the N-Queen puzzle                             |

### PS

This is a project done during **Full Stack Software Engineering studies** at **ALX_AFRICA**. The objectives of the project is teach **ALX-SE students** about object oriented programming (OOP), Data Abstraction, Data Encapsulation, instances and classes attributes in **Python**.
