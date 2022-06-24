#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as te:
        print("Exception: ", te)
        return False
    except ValueError as ve:
        print("Exception: ", ve)
        return False
