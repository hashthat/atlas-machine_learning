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


    derivative = []
    for i in range(1, len(poly)):

        derivative.append(poly[i] * i)
    return derivative
