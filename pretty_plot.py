# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   12.16
# Date:         28 November 2022
#
import numpy as np
from matplotlib import pyplot as plt
v = np.array([[0],[1]]) #creates first array
m = np.array([(1.01, .09), (-.09, 1.01)])
x = []
y = []
for i in range(201):
    v = m @ v         #multiplies array by the new "v" value 
    c = v.tolist()
    x.append(c[0])
    y.append(c[1])  #appends all the values to a list for matplotlib to present
plt.ylabel("y")
plt.xlabel("x")
plt.plot(x, y)
plt.title("Spiral")
plt.show()

