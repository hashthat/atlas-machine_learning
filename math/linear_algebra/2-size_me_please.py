#!/usr/bin/env python3
# finding the rows and columns of a matricies through len

def matrix_shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix and matrix[0] else 0
    return rows, cols
