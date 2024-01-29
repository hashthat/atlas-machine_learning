#!/usr/bin/env python3
"""
utilizing numpy.ndarray hence mat1 and mat2.
Return a tuple containing the element-wise sum,
difference, product and qutient.
mat1 and mat2 are never empty
https://bit.ly/np_arithmetic
"""


def np_elementwise(mat1, mat2):
    """
    the operation of this function performs elementwise
    addition, subtraction, multiplication, division
    """

    return (mat1 + mat2, mat1 * mat2, mat1 - mat2, mat1 / mat2)
