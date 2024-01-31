#!/usr/bin/env python3
"""
this is the basic loop seegma expressed in python!
n is the limiting factor a.k.a. the stopping condition.
Return: None if n is not a valid number.
"""


def summation_i_squared(n):
    """
    the summation of the equation utilizes the addition of the
    factorial of i^2 and n being the stopping number in which i
    increases to in the summation of the given problem or example.
    """
    if not isinstance(n, int) or n <= 0:
        return None

    if n == 1:
        return 1

    return n**2 + summation_i_squared(n - 1)
