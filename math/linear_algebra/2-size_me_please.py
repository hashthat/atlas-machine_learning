#!/usr/bin/env python3
"""
function to determine if there is a matrix
the function will express the shape
"""


def matrix_shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix and isinstance(matrix[0], list) else 1
    shape = [rows, cols]
    return tuple(shape)
    # check if the matrix is a list or integer
    if isinstance(matrix, list):

        rows = len(matrix)
        # cols = len(matrix[0]) if matrix and matrix[0] else 0
        shape = []
        # shaping shapes!
        shape.append(rows)
        if isinstance(matrix[0], list):
            shape.append(matrix_shape(matrix[0])[0])
        if isinstance(matrix[0], int):
            shape.append(len(matrix))
        # return the list and int shape of the matrix
        return shape
