#!/usr/bin/env python3
"""
concatonating two arrays
"""


def add_arrays(arr1, arr2):
    """
    this is just adding two lists together
    """
    if len(arr1) != len(arr2):
        return None

    cat = [a + b for a, b in zip(arr1, arr2)]
    return cat
