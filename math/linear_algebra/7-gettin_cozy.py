#!/usr/bin/env python3
"""
concatonate two matricies along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    assume all elements with same dimension have the same type/shape
    Return: a New Matrix or None if they cannot be concatonated
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        raise ValueError("this is not a Matricies.")
