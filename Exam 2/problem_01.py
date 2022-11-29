# Import modules
import numpy as np
import math
import matplotlib.pyplot as plt

# Define the function p
def P(x: float, u: float, s: float) -> float:
    return (1 / math.sqrt(2 * np.pi * (s ** 2)) * math.exp(-((x - u) ** 2) / (2 * (s ** 2))))

# Creating the values
x = np.arange(-3, 3, 0.1)
y = [P(x_val, 0, 1) for x_val in x]

# Plotting
plt.plot(x, y)
plt.xlabel("Input Values")
plt.ylabel("Results of P(X)")
plt.show()