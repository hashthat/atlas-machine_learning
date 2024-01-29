#!/usr/bin/env python3
"""
adding two matricies by their elements!
"""


def add_matrices2D(mat1, mat2):
    """
    elements in a zip context of two matricies 
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    # choosing ihat or jhat as the basis of the equation!

    ihat = [[a + b for a, b in zip(row1, row2)]
            for row1, row2 in zip(mat1, mat2)]
    
    # Add the Elements to shape the matricies

    return ihat
