#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        pos = number * -1
        ld = pos % 10
    else:
        ld = number % 10
    print(ld, end="")
    return(ld)
