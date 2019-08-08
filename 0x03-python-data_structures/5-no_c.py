#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for letter in my_list:
        if letter == 'c':
            my_list.remove('c')
        elif letter == 'C':
            my_list.remove('C')
    new_string = ""
    new_string = new_string.join(my_list)
    return new_string
