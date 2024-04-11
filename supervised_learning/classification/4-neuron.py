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

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def evaluate(self, X, Y):
        # Forward propagation to get predictions
        Z = np.dot(self.weights.T, X) + self.bias
        A = self.activate(Z)

        # Convert predictions to binary labels (1 if >= 0.5, 0 otherwise)
        predictions = np.where(A >= 0.5, 1, 0)

        # Compute cost (binary cross-entropy)
        m = X.shape[1]
        cost = -np.mean(Y * np.log(A) + (1 - Y) * np.log(1 - A))

        return predictions, cost
