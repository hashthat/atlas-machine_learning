#!/usr/bin/env python3

"""
matrix_transpose - J and I hat are the base of the vectors for the matrix position
Returns: Transposed Matrix

"""


def matrix_transpose(matrix):

    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed

