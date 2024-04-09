#!/usr/bin/env python3

import numpy as np


class NeuralNetwork():
    """
    This class is defining a NeuralNetwork
    basically a MatrixProduct utilizing the
    dot product in measuring the weights and
    biases of a net.
    """

    def __init__(self, nx, nodes):
        # NX < 1
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if type(nx) is int and nx < 1:
            raise ValueError("nx must be a positive integer")

        # Validate nodes
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if type(nodes) is int and nodes < 1:
            raise ValueError("nodes must be a positive integer")

        # Initialize weights and biases for the hidden layer
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0

        # Initialize weights and biases for the output neuron
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

        @property
        def W1(self):
            return self.__W1

        @property
        def b1(self):
            return self.__b1

        @property
        def A1(self):
            return self.__A1

        @property 
        def W2(self):
            return self.__W2

        @property
        def b2(self):
            return self.__b2

        @property
        def A2(self):
            return self.__A2
