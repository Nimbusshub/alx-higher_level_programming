#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except TypeError as te:
        print("Exception:", te, file=stderr)
        return False
    except ValueError as ve:
        print("Exception:", ve, file=stderr)
        return False
