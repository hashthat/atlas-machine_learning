#!/usr/bin/env python3
"""
multiplying 2 Matricies
https://stackoverflow.com/questions/10508021/matrix-multiplication-in-pure-python
"""


def mat_mul(mat1, mat2):
    """
    Parameters:
        - mat1: 2D list of ints/floats
        - mat2: 2D list of ints/floats

    Return:
        - New 2D list as a result of multiplying mat1 * mat2
        - Returns None if Matricies cannot be multiplied
    """
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0]) if mat1 else 0
    rows_mat2 = len(mat2)
    cols_mat2 = len(mat2[0]) if mat2 else 0

    if cols_mat1 != rows_mat2:
        return None
    """
    this is where the result of the function comes into play
    given the format of the matricies being multiplied
    """
    mtrx = [[sum(i * j for i, j in zip(row1, col2))
            for col2 in zip(*mat2)]
            for row1 in mat1]

    return mtrx
