#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
add = 0
for i in argv:
    if i == argv[0]:
        continue
    add += int(i)
print("{:d}".format(add))
