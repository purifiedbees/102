# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jacob Hou
#               Derick
#               Shane
#               Adan
# Section:      524
# Assignment:   Lab 12.14
# Date:         16 November 2022
#
# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material 
import numpy as np
a = np.array([(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11)])
b = np.array([(0, 1), (2, 3), (4, 5), (6, 7)])
c = np.array([(0, 1, 2), (3, 4, 5)])
d = a @ b @ c  #the @ symbol allows the multiplication of multiple matrices
e = np.transpose(d)   #print out that it is D^T
f = np.sqrt(d)/ 2
print(f"A = {a}")
print(f"B = {b}")
print(f"C = {c}")
print(f"D = {d}")
print(f"D^T = {e}")
print(f"E = {f}")