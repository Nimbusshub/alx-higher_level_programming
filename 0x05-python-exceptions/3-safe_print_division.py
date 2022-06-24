#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = round(a / b, 1)
    except ZeroDivisionError:
        c = None
    finally:
        print("{}: {}".format("Inside result", c))
    return c
