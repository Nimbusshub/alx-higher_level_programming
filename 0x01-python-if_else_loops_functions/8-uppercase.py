#!/usr/bin/python3
def uppercase(str):
    for j in str:
        if ord(j) >= 97 and ord(j) <= 122:
            n = 32
        else:
            n = 0
        print("{}".format(chr(ord(j) - n)), end="")
    print()
