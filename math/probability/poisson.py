#!/usr/bin/env python3
"""
creating the class Poisson
"""
class Poisson:
    """
    The poisson distribution, named after Siméon Denis Poisson
    is an expression where the probability of a fixed-size interval
    with a given number of events occuring in the fixed interval
    given time or space.
    poisson is Discrete meaning it can only take on whole
    numbers where the lambtha is a positive real number
    with a single parameter and represents the average
    rate of events.
    """

    def __init__(self, data=None, lambtha=1.0):
        """
        creating the prediction through an intuitive series
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
            self.data = None
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)
            self.data = data
