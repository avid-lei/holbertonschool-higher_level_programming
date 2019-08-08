#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or roman_string == {}:
        return None
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for letter in roman_string:
        for key in roman:
            if letter == key:
                sum = sum + roman[key]
    return sum
