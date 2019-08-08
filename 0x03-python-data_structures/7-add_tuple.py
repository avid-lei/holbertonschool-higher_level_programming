#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    if len(a) < 2:
        for i in range(len(a), 2):
            a.append(0)
    b = list(tuple_b)
    if len(b) < 2:
        for i in range(len(b), 2):
            b.append(0)
    c = []
    for i in range(2):
        c.append(b[i] + a[i])
    return tuple(c)
