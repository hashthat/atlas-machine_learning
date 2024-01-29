#!/usr/bin/env python3

"""
matrix_transpose: J and I hat are the base vectors
Returns: Transposed Linear Matrix

"""


def matrix_transpose(matrix):
    """
    function that expresses the change in matrix based on a 2D graph
    """
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed
