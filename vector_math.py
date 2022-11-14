# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   Lab 7.27
# Date:         12 October 2022
#
from math import *
magnitudeA = 0 #establishes magnitude for both vectors
magnitudeB = 0
vectorAddition = []  #establishes empty addition vector and variable to append to the list
addition = 0
vectorSubtraction = [] #same thing as the top comment
subtraction = 0
dotProduct1 = 0 #establishes dot product using two variables
dotProduct = 0
vectorA = input("Enter the elements for vector A:")
vectorA = vectorA.split()
vectorB = input("Enter the elements for vector B:")
vectorB = vectorB.split()
vectorintA = [] #establishes the vectors to change the type from str to float
vectorintB = []
vectorintA = [float(i) for i in vectorA]
vectorintB = [float(j) for j in vectorB]

#calculates magnitude for both vectors
for k in range(0, len(vectorintA)):
    magnitudeA += vectorintA[k] ** 2
magnitudeA = sqrt(magnitudeA)
for k in range(0, len(vectorintB)):
    magnitudeB += vectorintB[k] ** 2
magnitudeB = sqrt(magnitudeB)

#calculates the vector addition
for k in range(0, len(vectorA)):
    addition = (vectorintA[k] + vectorintB[k])
    vectorAddition.append(addition)

#calculates the vector subtraction
for k in range(0, len(vectorintA)):
    subtraction = (vectorintA[k] - vectorintB[k])
    vectorSubtraction.append(subtraction)

#calculates the vector dot product
for k in range(0, len(vectorintA)):
    dotProduct1 = vectorintA[k] * vectorintB[k]
    dotProduct += dotProduct1
print(f"The magnitude of vector A is {magnitudeA:.5f}")
print(f"The magnitude of vector B is {magnitudeB:.5f}")
print(f"A + B is {vectorAddition}")
print(f"A - B is {vectorSubtraction}")
print(f"The dot product is {dotProduct:.2f}")