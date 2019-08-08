#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for column in row:
            if count == len(row) - 1:
                print("{:d}".format(column), end='')
            else:
                print("{:d}".format(column), end=' ')
            count += 1
        print('')
