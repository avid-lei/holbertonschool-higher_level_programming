#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    pos = number * -1
    ld = pos % 10
else:
    ld = number % 10
if ld > 5:
    print("Last digit of " + str(number) + " is " + str(ld) + " and is greater than 5")
elif ld == 0:
    print("Last digit of " + str(number) + " is " + str(ld) + " and is 0")
else:
    print("Last digit of " + str(number) + " is " + str(ld) + " and is less than 6 and not 0")