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
def realValid(string):
    pidBool = True
    cidBool = True
    byrBool = True
    iyrBool = True
    eyrBool = True
    hgtBool = True
    eclBool = True
    hclBool = True
    if "byr" in string:
        try:
            if len(string) != 8 or (int(string[4:]) < 1920 or int(string[4:]) > 2005):
                byrBool = False
        except:
            byrBool = False
    if "iyr" in string:
        try:
            if len(string) != 8 or (int(string[4:]) < 2012 or int(string[4:]) > 2022):
                iyrBool = False
        except:
            iyrBool = False
    if "eyr" in string:
        try:
            if len(string) != 8 or (int(string[4:]) < 2022 or int(string[4:]) > 2032):
                eyrBool = False
        except:
            eyrBool = False
    if "hgt" in string:
        if string[-2:] == "cm":
            if len(string) != 9 or (int(string[4:7]) < 150 or int(string[4:7]) > 193):
                hgtBool = False
        elif string[-2:] == "in":
            if len(string) != 8 or (int(string[4:6]) < 59 or int(string[4:6]) > 76):
                hgtBool = False
        else:
            hgtBool = False
    if "ecl" in string:
        colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if len(string) != 7 or (not(string[4:]) in colors):
            eclBool = False
    if "pid" in string:
        if len(string) != 13:
            pidBool = False
        else:
            if string[4:].isnumeric():
                pidBool = True
            else:
                pidBool = False
    if "cid" in string: 
        if len(string) != 7:
            cidBool = False
        else:
            try:
                if int(string[4:]) < 100:
                    cidBool = False
            except:
                cidBool = False
    if pidBool and cidBool and byrBool and iyrBool and eyrBool and hgtBool and eclBool and hclBool:
        return True

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
#part 2 

for i in realPassports:
    if validityChecker(i):
        validrealnum += 1
        validPassportsList.append(i)
legalReal = []

counter = 0
for legal in validPassportsList:
    validIndivduals = legal.split(" ")
    indivdualList = []
    passportREAL = True
    for i in validIndivduals:
        if i != "\n" and i != "":
            indivdualList.append(i)
    for j in indivdualList:
        if realValid(j):
            passportREAL = True
        else:
            passportREAL = False
            break
    if passportREAL:
        legalReal.append(legal)
        counter += 1
print(f"There are {counter} valid passports")
validPassportsFile = open("valid_passports2.txt", "w")
for i in legalReal:
    k = i.split("  ")
    for j in k:
        validPassportsFile.write(j + "\n")
validPassportsFile.close()
