#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    count = 0
    for x in my_list:
        if count == idx:
            return x
        else:
            count += 1
    return None
