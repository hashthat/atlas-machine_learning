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
