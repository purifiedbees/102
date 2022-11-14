# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   Lab 9
# Date:         26 October 2022
#
from math import *
import numbers
def parta(a, r):
    volume = 0 #finds volume through the equation
    volume = (4/3) * (a ** 2 - r ** 2) ** 1.5 * pi
    return volume

def partb(n):
    numbers = [] #list to store all the odd numbers that add up to n
    for i in range(1, n, 2): #in each loop, counts by 2 and starts at 1 since we are finding odd numbers
        total = 0
        for j in range(i, n, 2): #loop checks when j hits n, it adds to total which checks if total equals to the input
            total += j
            if total == n:
                numbers.append([])
                for k in range(i, j+1, 2):
                    numbers[-1].append(k) #appends the next number at the end 
                break
            elif total > n:
                break
    space = " " #used to break each number between to get a space
    if not(bool(numbers)): #if there are no numbers possible, return false
        return False
    for i in numbers:
        return i
    return space

def partc(char, name, company, email):
    maxLength = len(name) #assumes maxLength to be the length of the name
    if len(company) > len(name):   #sees if the other elements are longer than the name
        maxLength = len(company)
    if len(email) > maxLength:
        maxLength = len(email)
    length = maxLength + 6   #increases the spacing around the finalString
    finalString = length * char + "\n" #gets the char that is inputted to make the first part of the "box"
    finalString += char + name.center(length - 2) + char + "\n" #center() lets the name/company/email to be in the center of the box
    finalString += char + company.center(length - 2) + char + "\n"
    finalString += char + email.center(length - 2) + char + "\n"
    finalString += length * char
    return finalString

def partd(numbers):
    numbers = sorted(numbers) #the sorted() function helps sort the list ascending 
    median = 0
    numbersLength = len(numbers) #length of the entire list
    if numbersLength % 2 == 0:   #finding the median is determined if the length is either odd or even
        median = (numbers[numbersLength // 2 - 1] + numbers[numbersLength // 2]) / 2
    else:
        median = numbers[numbersLength // 2]
    return numbers[0], median, numbers[-1]

def parte(time, distance):
    velocity = []
    for i in range(len(time) - 1):
        velocity.append((distance[i+1] - distance[i])/(time[i+1] - time[i]))  #equation to find the velocity between the two times/distances
    return velocity

def partf(listnum):
    product = []
    for i in listnum:   #goes through each number to see if they add up to 2026, if they do, multiply and add the product to product list
        for j in listnum:
            if 2026 == i + j:
                z = i * j
                product.append(z)
    list(product)   #convert it to a list and sort ascending
    product = sorted(product)
    if not bool(product):   #if none equal to, return false, if true return the product vaue
        return False
    return product[0]