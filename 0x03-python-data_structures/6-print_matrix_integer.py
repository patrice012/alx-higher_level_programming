#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 1
        for cell in row:
            if count != len(row):
                print('{:d}'.format(cell), end=" ")
            else:
                print('{:d}'.format(cell))
            count += 1
    if matrix == [[]]:
        print()
