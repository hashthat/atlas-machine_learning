#!/usr/bin/env python3
"""
poly is a list of coefficients representing a polynomial
C is the Constant
Return: None if poly or C are not valid.
the returned list should be as small as possible
"""


def poly_integral(poly, C=0):
    """
    a function that calculates the integral of a polynomial
    """

    if not isinstance(poly, list) or not all(isinstance(coef, (int, float)) for coef in poly) or not isinstance(C, int):
        return None

    integral_coeffs = [C]

    for i, coef in enumerate(poly):
        if not isinstance(coef, (int, floa)):
            return None

        power = i + 1
        new_coef = coef / power
        integral_coeffs.append(new_coef)

    return integral_coeffs
