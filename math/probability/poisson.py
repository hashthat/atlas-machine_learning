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

    def pmf(self, k):
        """Calculate the PMF value for a given number of 'successes' (k)."""
        k = int(k)  # Convert k to an integer

        if k < 0:
            return 0  # k is out of range, return 0
        else:
            return (math.exp(-self.lambtha)*self.lambtha**k)/math.factorial(k)

    def cdf(self, k):
        """Calculate the CDF value for a given number of 'successes' (k)."""
        k = int(k)  # Convert k to an integer

        if k < 0:
            return 0  # k is out of range, return 0
        else:
            cdf_value = 0
            for i in range(k + 1):
                cdf_value += self.pmf(i)
            return cdf_value
