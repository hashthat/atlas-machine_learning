#!/usr/bin/env python3

def matrix_shape(matrix):
    
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
        elif type(matrix[0]) is int:
            shape.append(len(matrix))
        # return the list and int shape of the matrix
        return shape
