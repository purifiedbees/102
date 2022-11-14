# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jacob Hou
#               Derick
#               Shane
#               Adan
# Section:      524
# Assignment:   Lab 11.9
# Date:         13 November 2022
#
import csv
def validityChecker(string):
    if "pid" in string and "cid" in string and "byr" in string and "iyr" in string and "eyr" in string and "hgt" in string and "ecl" in string and "hcl" in string:
        return True
    elif "pid" in string and "cid" in string and "byr" in string and "iyr" in string and "eyr" in string and "hgt" in string and "ecl" in string:
        return True
    else:
        return False
validrealnum = 0
passports = []
validPassportsList = []
realPassports = []
realPassportsStr = ""
file = input("Enter the name of the file: ")
with open(file) as file:
    sdafafdsafs = csv.reader(file, delimiter = "\n")
    for passport in sdafafdsafs:
        passports.append(passport)
#gets the valid passports without empty lines
for passport in range(len(passports)):
    try:
        if passports[passport][0] != "\n":
            realPassportsStr += str(passports[passport][0]) + "  "
    except:
        realPassports.append(realPassportsStr)
        realPassportsStr = ""

for i in realPassports:
    if validityChecker(i):
        validrealnum += 1
        validPassportsList.append(i)
print(f"There are {validrealnum} valid passports")
validPassportsFile = open("valid_passports.txt", "w")
for i in validPassportsList:
    k = i.split("  ")
    for j in k:
        validPassportsFile.write(j + "\n")
validPassportsFile.close()
