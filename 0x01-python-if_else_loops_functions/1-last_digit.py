#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = int(repr(number)[-1])
if number < 0:
    lastD *= -1
print("Last digit of {} is {}".format(number, lastD), end=" ")
if lastD < 6 and lastD != 0:
    print("and is less than 6 and not 0")
elif lastD > 5:
    print("and is greater than 5")
elif lastD == 0:
    print("and is 0")
