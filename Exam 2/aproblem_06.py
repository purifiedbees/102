import numpy as np
import math
import matplotlib.pyplot as plt

# Defining the function p
def P(x: float, u: float, s: float) -> float:
    return (1 / math.sqrt(2 * np.pi * (s ** 2)) * math.exp(-((x - u) ** 2) / (2 * (s ** 2))))


# Creating the values
x = []
y = []

current_x = -3
current_y = P(current_x, 0, 1)

while current_x <= 3:
    x.append(current_x)
    y.append(current_y)

    current_x += 0.1
    current_y = P(current_x, 0, 1)

# Plotting
plt.plot(x, y)
plt.xlabel("Input Values")
plt.ylabel("Results of P(x)")
plt.show()

