#!/usr/bin/env python3
"""
function to determine if there is a matrix
the function will express the shape
"""


def matrix_shape(matrix):
<<<<<<< HEAD

    rows = len(matrix)
    cols = len(matrix[0]) if matrix and isinstance(matrix[0], list) else 1
    shape = [rows, cols]
    return tuple(shape)
=======
    
    # check if the matrix is a list or integer
    if isinstance(matrix, list):
    # is the number a list or an integer?? I need some Recursive help!!!
    # find the rows and columns of the matrix for the expression needed to solve the equation.
        
        rows = len(matrix)
        # cols = len(matrix[0]) if matrix and matrix[0] else 0
        shape = []
        
        
        shape.append(rows)
        if isinstance(matrix[0], list):
            shape.append(matrix_shape(matrix[0])[0])
        if isinstance(matrix[0], int):
            shape.append(len(matrix))
        # return the list and int shape of the matrix
        return shape
>>>>>>> parent of e1b848a (append)
