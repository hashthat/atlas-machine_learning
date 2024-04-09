#!/usr/bin/env python3
""" creating a neural network from scratch!!"""
import numpy as np


class NeuralNetwork():
    """
    This class is defining a NeuralNetwork
    basically a MatrixProduct utilizing the
    dot product in measuring the weights and
    biases of a net.
    """

    def __init__(self, nx, nodes):
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx <= 0:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes <= 0:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
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

    def sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))

    """
    sigmoid is the strategy to convert weighted sums
    into the context of probability given
    the output of the function of the neural network
    """


    def forward_prop(self, X):
        # Activation of the computed hidden layer
        Z1 = np.dot(self.W1, X) + self.b1
        self.__A1 = self.sigmoid(Z1)

        Z2 = np.dot(self.__W2, self.__A1) + self.b2
        self.__A2 = self.sigmoid(Z2)

        return self.__A1, self.__A2