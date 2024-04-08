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
        pre = self.forward_prop(X)

        # Convert predictions to binary labels
        binary_predictions = np.where(pre >= 0.5, 1, 0)

        # Calculate cost using logistic regression formula
        m = Y.shape[1]
        cost = -(1/m) * np.sum(Y * np.log(pre) + (1 - Y) * np.log(1 - pre))

        return binary_predictions, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        # Calculate gradients
        m = Y.shape[1]
        dz = A - Y
        dw = np.dot(X, dz.T) / m
        db = np.sum(dz) / m

        # Update weights and bias
        self.__W -= alpha * dw.flatten()
        self.__b -= alpha * db

        return self.evaluate(X, Y)

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        # Validate iterations, alpha, and step
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if not isinstance(step, int):
            raise TypeError("step must be an integer")
        if step <= 0 or step > iterations:
            raise ValueError("step must be positive and <= iterations")

        # Initialize cost history
        cost_history = []

        # Train the neuron
        for i in range(iterations + 1):
            # Forward propagation
            A = self.forward_prop(X)

            # Backward propagation (gradient descent)
            self.gradient_descent(X, Y, A, alpha)

            # Calculate cost every step iterations
            if verbose and i % step == 0:
                _, cost = self.evaluate(X, Y)
                cost_history.append(cost)
                print(f"Cost after {i} iterations: {cost}")

        # Plot cost history if graph is True
        if graph:
            iterations_axis = range(0, iterations + 1, step)
            plt.plot(iterations_axis, cost_history, 'b-')
            plt.xlabel('Iteration')
            plt.ylabel('Cost')
            plt.title('Training Cost')
            plt.show()

        # Evaluate the training data
        return self.evaluate(X, Y)
