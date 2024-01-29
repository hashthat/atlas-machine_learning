#!/usr/bin/env python3

def matrix_shape(matrix):
    # check if the matrix is empty!
    
    if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        riase ValueError("the input recieved is not a valid matrix, this is your valid TypeError warning")

    # find the rows and columns of the matrix for the expression needed to solve the equation.
    rows = len(matrix)
    cols = len(matrix[0]) if matrix and matrix[0] else 0
    # shape = [rows, cols] # variable name of rows and cols

    # return the shape with a tuple
    # error for getting the proper length of the matrix
    
    return rows, cols
