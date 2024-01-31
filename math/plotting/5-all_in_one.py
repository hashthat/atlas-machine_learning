#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Data for the plots
y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Plot configurations
plt.figure(figsize=(10, 10))

# Plot 1 (3x2 grid, first plot)
plt.subplot(3, 2, 1)
plt.plot(y0, label='y0')
plt.title('y0')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.tick_params(axis='both', labelsize='x-small')

# Plot 2 (3x2 grid, second plot)
plt.subplot(3, 2, 2)
plt.scatter(x1, y1, alpha=0.5, color='blue', label='Scatter Plot')
plt.title('Scatter Plot of Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.tick_params(axis='both', labelsize='x-small')

# Plot 3 (3x2 grid, third plot)
plt.subplot(3, 2, 3)
plt.plot(x2, y2, label='Exponential Decay', color='blue')
plt.title('Exponential Decay of C-14')
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.yscale('log')
plt.xlim(0, 28650)
plt.tick_params(axis='both', labelsize='x-small')

# Plot 4 (3x2 grid, fourth plot)
plt.subplot(3, 2, 4)
plt.plot(x3, y31, label='C-14', color='red', linestyle='--')
plt.plot(x3, y32, label='Ra-226', color='green', linestyle='-')
plt.title('Exponential Decay of Radioactive Elements')
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.xlim(0, 20000)
plt.ylim(1e-6, 1)
plt.yscale('log')
plt.legend(loc='upper right')
plt.tick_params(axis='both', labelsize='x-small')

# Plot 5 (3x2 grid, fifth plot, spans two columns)
plt.subplot(3, 2, (5, 6))
plt.hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')
plt.title('Histogram of Student Grades')
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.tick_params(axis='both', labelsize='x-small')

# Adjust layout
plt.tight_layout()

# Title of the figure
plt.suptitle('All in One', fontsize='x-large')

# Display the plots
plt.show()
