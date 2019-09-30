#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = {'+': add(a, b), '-': sub(a, b), '*': mul(a, b), '/': div(a, b)}
    if not argv[2] in ops.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    res = ops[argv[2]]
    print("{:d} {} {:d} = {:d}". format(a, argv[2], b, res))
