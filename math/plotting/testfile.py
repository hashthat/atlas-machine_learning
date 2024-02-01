#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the quadratic function and its derivative
def y_function(x):
    return x ** 2

def y_derivative(x):
    return 2 * x

# Gradient Descent Function
def gradient_descent(starting_point, learning_rate, iterations):
    trajectory = [starting_point]

    for _ in range(iterations):
        current_pos = trajectory[-1]
        new_x = current_pos - learning_rate * y_derivative(current_pos)
        trajectory.append(new_x)

    return np.array(trajectory)

# Visualization
def plot_gradient_descent(x, y, trajectory):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x, y, y_function(x), label='y = x^2', color='blue')
    ax.scatter(trajectory[:, 0], y_function(trajectory[:, 0]), trajectory[:, 1], color='red', label='Gradient Descent')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.legend()

    plt.show()

# Set up the data
x = np.linspace(-10, 10, 100)
y = y_function(x)

# Run gradient descent from starting point 8 with a learning rate of 0.1 for 100 iterations
trajectory = gradient_descent(starting_point=8, learning_rate=0.1, iterations=100)

# Plot the 3D graph
plot_gradient_descent(x, y, trajectory)

