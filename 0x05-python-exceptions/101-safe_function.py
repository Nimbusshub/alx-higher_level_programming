#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        cont = fct(*args)
        return cont
    except Exception as error:
        cont = None
        print("{}: {}".format("Exception", error), file=stderr)
        return cont
