#!/usr/bin/env python3
""" creating a neural network from scratch!!"""
import numpy as np


class NeuralNetwork():
    """
    This class is defining a NeuralNetwork
    basically a MatrixProduct utilizing the
    dot product in measuring the weights and
    biases of a net.
    sigmoid: a function for mathematical expression
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

    def cost(self, Y, A):
        """
        Y is numpy.ndarra
        A is numpy.ndarray
        both with shape 1, m
        """
        epsilon = 1.0000001
        m = Y.shape[1]
        cost = -(1/m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(epsilon - A))

        return cost

    def evaluate(self, X, Y):
        # Perform forward propagation
        _, A2 = self.forward_prop(X)

        # Compute predictions
        predictions = np.where(A2 >= 0.5, 1, 0)

        # Compute cost
        cost = self.cost(Y, A2)

        return predictions, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        m = Y.shape[1]
        
        # Compute gradients for output layer
        dZ2 = A2 - Y
        dW2 = (1/m) * np.dot(dZ2, A1.T)
        db2 = (1/m) * np.sum(dZ2, axis=1, keepdims=True)
        
        # Compute gradients for hidden layer
        dZ1 = np.dot(self.__W2.T, dZ2) * (A1 * (1 - A1))
        dW1 = (1/m) * np.dot(dZ1, X.T)
        db1 = (1/m) * np.sum(dZ1, axis=1, keepdims=True)
        
        # Update weights and biases
        self.__W2 -= alpha * dW2
        self.__b2 -= alpha * db2
        self.__W1 -= alpha * dW1
        self.__b1 -= alpha * db1
        
    def train(self, X, Y, iterations=5000, alpha=0.05):
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        
        for i in range(iterations):
            A1, A2 = self.forward_prop(X)
            self.gradient_descent(X, Y, A1, A2, alpha)

        return self.__A2