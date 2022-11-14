# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   Lab 7.28
# Date:         12 October 2022
#

constant = input("Enter a four-digit integer:")
constantList = []
asc = []
desc = []
constantListReverse = []
originalConstant = constant
finalConstant = 0
path = constant
count = 0

for i in originalConstant:
    constantList.append(i)
while len(constantList) != 4:
    constantList.append("0")

#starts loop
while finalConstant != 6174:
    ascStr = ""
    descStr = ""

    if(constantList[0] == constantList[1] == constantList[2] == constantList[3]):
        finalConstant = 0000
        print(path + " > 0")
        print(f"{originalConstant} reaches 0 via Kaprekar's routine in 1 iterations")
        break
    constantList.sort()
    for j in constantList:
        ascStr += j
    constantListReverse = [constantList[3], constantList[2], constantList[1], constantList[0]]
    for j in constantListReverse:
        descStr += j

    finalConstant = int(descStr) - int(ascStr)
    path += " > " + str(finalConstant)
    constantList = list(str(finalConstant))
    count += 1
    while len(constantList) != 4:
        constantList.append("0")
if(finalConstant != 0000):
    print(path)
    print(f"{originalConstant} reaches 6174 via Kaprekar's routine in {count} iterations")