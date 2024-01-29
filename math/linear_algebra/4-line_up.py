#!/usr/bin/env python3
"""
concatonating two arrays
given their elements (zip)

arr1 and arr2 are lists of integers and floats.

Returns:
    - New List representing (arr1 + arr2)
    if arr1 and arr2 are not the same shape
    return None!
"""


def add_arrays(arr1, arr2):
    """
    this is just adding two lists together
    """
    if len(arr1) != len(arr2):
        return None

    cat = [a + b for a, b in zip(arr1, arr2)]
    return cat
