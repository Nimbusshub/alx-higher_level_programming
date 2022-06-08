#!/usr/bin/python3
def square_it(j):
    return j ** 2


def square_matrix_simple(matrix=[]):
    new_list = []
    square = []
    for i in matrix:
        new_list = list(map(lambda j: j ** 2, i))
        square.append(new_list)
    return square
