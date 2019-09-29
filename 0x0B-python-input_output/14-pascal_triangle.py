#!/usr/bin/python3

"""
pascal triangle
return lists of lists of integers

"""


def pascal_triangle(n):
    tri = [[]]
    if n <= 0:
        return tri
    for li in range(1, n + 1):
        tri.append([])
        for ele in range(li):
            if ele == 0 or ele == li - 1:
                tri[li].append(1)
            else:
                tri[li].append(tri[li-1][ele] + tri[li-1][ele-1])

    return tri[1:]
