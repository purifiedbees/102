# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   Lab 7.26
# Date:         12 October 2022
#

sentenceInput = input("Enter some text:")
sentenceSplit = sentenceInput.split()
leetSpeak = {"a":"4", "e":"3", "o":"0", "s":"5", "t":"7"} #dictionary to access the specific letters to the numbers
finalSentence = " "
for word in sentenceSplit:
    letter = []
    for char in word:
        letter.append(char)
        for leet in leetSpeak:
            if leet == char:
                char = leetSpeak[leet]
        finalSentence = finalSentence + char
    if word != sentenceSplit[-1]:
        finalSentence += " "
print(f"In leet speak, \"{sentenceInput}\" is: {finalSentence}")


