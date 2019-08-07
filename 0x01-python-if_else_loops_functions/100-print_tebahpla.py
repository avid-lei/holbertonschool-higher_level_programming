#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        cap = 0
    else:
        cap = 32
    print("{:c}".format(letter - cap), end="")
