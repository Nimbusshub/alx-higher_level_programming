#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

if len(argv) - 1 == 0:
    print("{:d} arguments.".format(0))
elif len(argv) - 1 == 1:
    print("{:d} argument:".format(1))
else:
    print("{:d} arguments:".format(len(argv) - 1))
i = 1
for strr in argv:
    if strr == argv[0]:
        continue
    print("{:d}: {}".format(i, strr))
    i += 1
