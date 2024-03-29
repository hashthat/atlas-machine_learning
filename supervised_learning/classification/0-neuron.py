#!/usr/bin/env python3

import numpy as np

'''
creating a neuron class
'''


class Neuron:

    """
    this is the class of developing a Neuron
    nx is the number of input features
    W ~ Weights vector for the neuron
    b ~ the Bias
    A ~ Activation output (prediction) of the neuron.
    upon the instantiation, the activation output should be
    initialized to 0.
    """

    
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
