#!/usr/bin/env python3
"""
writing a function that calculates
the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    poly is a list of coefficients representing
    a polynomial.
    [5, 3, 0, 1] = f(x) = x3, + 3x + 5
    Return: coefficients representing the derivative
    """

    if len(poly) < 2:
        return [0]

    coeffs = [poly[i] * i for i in range(len(poly)-1, 0, -1)]
    return coeffs
