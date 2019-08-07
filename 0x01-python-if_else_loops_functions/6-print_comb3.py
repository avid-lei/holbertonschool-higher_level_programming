#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(num1 + 1, 10):
        print("{:d}".format(num1), end="")
        if num1 == 8:
            print("{:d}".format(num2))
        else:
            print("{:d}, ".format(num2), end="")
