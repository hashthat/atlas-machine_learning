#!/usr/bin/env python3
import numpy as np
"""
this is a function that concatenates two
matricies along a specific axis

mat1 and mat2 can be interpreted by numpy.ndarray
Return: numpy.ndarray
mat1 and mat2 are never empty -- this is the assumption
"""


def np_cat(mat1, mat2, axis=0):
    # https://bit.ly/np_cat

    """
    Leveraging Numpy with np.concatonate
    as the function is transformed from the input
    to the output of this specific procedure
    with numpy. Leveraging the numpy API
    """
    return np.concatenate((mat1, mat2), axis=axis)
