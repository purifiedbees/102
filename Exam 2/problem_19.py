import matplotlib.pyplot as plt
import math

# Local extremities
def local_points(x: list[float], y: list[float]):
    # Store points
    mins = []
    maxes = []

    for i in range(1, len(y) - 1):
        # Local minimas
        if y[i-1] > y[i] and y[i+1] > y[i]:
            mins.append((x[i], y[i]))
            print(f"MIN FOUND: {x[i]}, {y[i]}")
        # Local maxima
        if y[i-1] < y[i] and y[i+1] < y[i]:
            maxes.append((x[i], y[i]))
            print(f"MAX FOUND: {x[i]}, {y[i]}")

    return mins, maxes

# Generate y based on equation
def y(x: float) -> float:
    return (0.1 * x**3) - (3 * math.cos(-2 * x))

# Set up my storage variables
x_points, y_points = [0], [y(0)]
step = 0.04

# Point generating loop
while x_points[-1] != 4.0:
    x_points.append(round(x_points[-1] + step, 2))
    y_points.append(y(x_points[-1]))

# Find local extremities
mins, maxes = local_points(x_points, y_points)

# Plot the function
plt.plot(x_points, y_points)

# Plot and annotate the local extremities
for point in mins:
    plt.plot(point[0], point[1], marker=".", color="blue")
    plt.annotate("Local Minima", xy=point, xytext=(point[0] + 0.1, point[1] - 1), 
                 arrowprops=dict(arrowstyle="->", color="red"))

for point in maxes:
    plt.plot(point[0], point[1], marker=".", color="red")
    plt.annotate(f"Local maxima", xy=point, xytext=(point[0] - 0.75, point[1] + 1.5),
                 arrowprops=dict(arrowstyle="->", color="red"))

# Adjust the graph
plt.title("Plot of x and y for y=0.1*x**3 - 3*cos(-2x)")
plt.xlabel("X data")
plt.ylabel("Y data")

plt.show()
