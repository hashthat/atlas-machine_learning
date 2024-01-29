#!/usr/bin/env python3

def matrix_shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix and matrix[0] else 0
    shape = [rows, cols]
    
    return tuple(shape)
