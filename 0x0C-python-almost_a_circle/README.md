# Python - Almost a circle

## Classes 🆑

The classes created for the project are

- Base - superclass
- Rectangle -subclass of Base
- Square -subclass of Rectangle

The three classes involved utilized the following Python tools:

- Import
- Exceptions
- Private attributes
- Getter/setter
- Class/static methods
- Inheritance
- File I/O
- `args`/`kwargs`
- JSON and CSV serialization/deserialization
- Unittesting

## Files in the Directory

Inside `models` folder:

| Filename       | Description                                                   |
| -------------- | ------------------------------------------------------------- |
| `__init__.py`  | Script that converts the directory as a package               |
| `base.py`      | Base class of geometrical instances                           |
| `rectangle.py` | Class that inherits attributes references from `Base` class   |
| `square.py`    | Class that inherits attributes references from `Square` class |

Each class contains public/private attibutes, class and static methods. Also, these class raise exceptions when is required.

Inside `tests/test_models` folder:

**The folder that tests the classes functionality**

| Filename            | Description                                         |
| ------------------- | --------------------------------------------------- |
| `__init__.py`       | Script that converts the directory as a package     |
| `test_base.py`      | Module that contains unittests to `Base` class      |
| `test_rectangle.py` | Module that contains unittests to `Rectangle` class |
| `test_square.py`    | Module that contains unittests to `Square` class    |
