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

    def forward_prop(self, X):
        # weighted sum calculation
        weighted_sum = np.dot(self.W, X) + self.b
        # apply Sigmoid activation function
        self.__A = self.sigmoid(weighted_sum)

        return self.__A
    
    def evaluate(self, X, Y):
        # Perform forward propagation to get predictions
        predictions = self.forward_prop(X)

        # Convert predictions to binary labels
        binary_predictions = np.where(predictions >= 0.5, 1, 0)

        # Calculate cost using logistic regression formula
        m = Y.shape[1]
        cost = -(1/m) * np.sum(Y * np.log(predictions) + (1 - Y) * np.log(1 - predictions))

        return binary_predictions, cost
