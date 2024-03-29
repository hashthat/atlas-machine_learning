#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180


plt.title("Men's Height vs Weight")
plt.ylabel("Weight (lbs)")
plt.xlabel("Height (in)")
plt.scatter(x, y, alpha=0.5, color='magenta') # Creates the scatter plot with the spec
plt.show()
