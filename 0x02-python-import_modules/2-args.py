#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    if (n == 0 or n == 1):
        print("0 arguments.")
    else:
        if (n == 2):
            print("1 argument:")
        else:
            print("{:d} arguments:".format(n - 1))
        for args in range(n - 1):
            print("{:d}: {:s}".format(args + 1, sys.argv[args + 1]))
