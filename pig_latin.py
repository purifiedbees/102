# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   Lab 7.25
# Date:         12 October 2022
#

ay = "ay"
way = "yay"
consonant = ["b","c", "d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
vowel = ["a","e","i","o","u", "y"]
pigLatinString = " "
sentenceInput = input("Enter word(s) to convert to Pig Latin:")
wordsSplit = sentenceInput.split()
for finalWords in wordsSplit:
    #gets first letter and checks if it is a valid string to process
    firstLetter = finalWords[0]
    firstLetter = str(firstLetter)
    length = len(finalWords)
    if length == 1:
        if firstLetter in vowel:
            pigLatin = finalWords + way
            pigLatinString = pigLatinString + " " + pigLatin
        elif firstLetter in consonant:
            length = len(finalWords)
            removeFirstLetter = finalWords[1:length]
            pigLatin = removeFirstLetter + firstLetter + ay + " "
            pigLatinString = pigLatinString + " " + pigLatin
    
    if length > 1:
        secondLetter = finalWords[1]
        secondLetter = str(secondLetter)
        if firstLetter in vowel:
            pigLatin = finalWords + way
            pigLatinString = pigLatinString + " " + pigLatin
            secondLetter = finalWords[1]
            secondLetter = str(secondLetter)
        elif secondLetter in consonant:
            length = len(finalWords)
            removeCluster = finalWords[2:length]
            pigLatin = removeCluster + firstLetter + secondLetter + ay + " "
            pigLatinString = pigLatinString + " " + pigLatin
        elif firstLetter in consonant:
            length = len(finalWords)
            removeFirstLetter = finalWords[1:length]
            pigLatin = removeFirstLetter + firstLetter + ay + " "
            pigLatinString = pigLatinString + " " + pigLatin
    
    
print(f"In Pig Latin, \"{sentenceInput}\" is: {pigLatinString}")