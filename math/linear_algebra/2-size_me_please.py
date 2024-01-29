#!/usr/bin/env python3

def matrix_shape(matrix):
    # check if the matrix is empty!

    if not matrix or not matrix[0]:
        return (0,0)

    # find the rows and columns of the matrix for the expression needed to solve the equation.
    rows = len(matrix)
    cols = len(matrix[0]) if matrix and matrix[0] else 0
    shape = [rows, cols] # variable name of rows and cols

    # return the shape with a tuple
    # error for getting the proper length of the matrix
    
    return tuple(shape)
