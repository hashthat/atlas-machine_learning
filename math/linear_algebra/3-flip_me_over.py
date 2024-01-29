#!/usr/bin/env python3

def matrix_transpose(matrix):

    """
    Transpose the matrix given from the test/main file

    Parameters:
    - matrix: a 2D list that represents the matrix

    Returns:
    - transposed matrix with how the matrix was "trasformed" given the graph.

    the I-hat and J-hat are the emphasis of the equation being the Base position of transformation.

    """
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    return transposed_matrix
