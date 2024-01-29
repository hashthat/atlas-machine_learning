#!/usr/bin/env python3
"""
function to determine if there is a matrix
the function will express the shape
"""


def matrix_shape(matrix):
    """
    tuple or a list given the shape
    shaping linear shapes is key
    """
    if type(matrix[0]) is not list:
        return ((len(matrix),))
    else:
        rows = len(matrix)
        cols = len(matrix[0]) if matrix[0] else 0
        return [rows, cols]
