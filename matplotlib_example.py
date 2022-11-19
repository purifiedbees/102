# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jacob Hou
#               Derick
#               Shane
#               Adan
# Section:      524
# Assignment:   Lab 12.15
# Date:         16 November 2022
#
# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material
from matplotlib import pyplot as plt
import numpy as np

#first plot
def f(x):
    return (1/8)* x **2
x = np.linspace(-2, 2) #linspace helps border the x-axis
plt.plot(x, f(x), color = "red", lw = 2)
def f(y):
    return (1/24) * y ** 2
y = np.linspace(-2, 2)
plt.ylabel("y")
plt.xlabel("x")
plt.title("Parabola plots with varying focal length")
plt.plot(y, f(y), color = "blue", lw = 6) # lw is the line thickness
plt.legend(["f=2", "f=6"], loc = "lower left")
plt.show()
#second plot
def f(t):
    return 2*t**3 + 3*t**2 - 11*t - 6
t = np.linspace(-4, 4)
plt.plot(t, f(t), "y*", mec = "black", ms = 10, markevery = 2)
plt.ylabel("y values")
plt.xlabel("x values")
plt.title("Plot of a cubic polynomial")
plt.show()

#third plot
def f(z):
    return np.sin(z)
def f(c):
    return np.cos(c)
plt.figure(1)
plt.subplot(212)
z = np.linspace(-2*np.pi, 2*np.pi)
plt.plot(z, f(z), color = "gray")
plt.grid(True)
plt.ylabel("y=sin(x)")
plt.legend(["sin(x)"], loc = "lower right")
plt.subplot(211)
c = np.linspace(-2*np.pi, 2*np.pi)
plt.plot(c, f(c), color = "red")
plt.ylabel("y=cos(x)")
plt.legend(["cos(x)"], loc = "lower right")
plt.title("Plot of cos(x) and sin(x)")
plt.grid(True)
plt.show()
