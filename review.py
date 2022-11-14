"""
#Questions 1 through 8 autograded
a = 5 
b = 'b' 
c = True 
print("The answer is...", end=' ') 
if a != 10: 
    print("A", end=' ') 
elif b == 'b': 
    print("B", end=' ') 
else: 
    print("C", end=' ') 
z = c and bool(a) 
print(z, end=' ') 
d = a ** 3 + 25 % 3 - 12 // 5 
print(d) 

#It would print out: The answer is... A True 124

n = 1 
p = "A" 
while n < 10: 
    p += p 
    n += 3 
print(n, p) 

#It would print out: 10, AAAAAAAA


a = True 
b = bool('False') 
c = 5 > 8 
d = a and b and c 
e = not a or not (b and c) 
print(d, e) 

#It would print out: False True


mystrs = ['Good Bull', 'Whoop', 'Hullabaloo', 'Howdy', "Gig 'em", 'Aggies'] 
mynums = [3, 5, 4, 1, 2] 
for num in mynums: 
    print(mystrs[num], end=' ') 
    print()
#It would print out: Howdy Aggies Gig 'em Whoop Hullabaloo


mydict = {'Ann' : 18, 'Bob' : 20, 'Charlie' : 19} 
if 'Joe' in mydict: 
    print("Joe is here") 
elif 'Ann' in mydict: 
    print("Hi Ann") 
else: 
    print("Anyone?") 

#It would print out: Hi Ann



mystr = 'The quick brown fox jumped over the lazy dog' 
print(mystr[:3], end=' ') 
if mystr[4] == 'q': 
    if 'fox' in mystr: 
        print('fox', end=' ') 
    else: 
        print('dog', end=' ') 
    if mystr[-5] != 'z': 
        print('jumped', end=' ') 
    else: 
        print('hopped', end=' ') 
elif 'x' in mystr: 
    if 'white' in mystr: 
        print('white mouse', end=' ') 
    else: 
        print('brown cow', end=' ') 
    if 'y' not in mystr: 
        print('sat', end=' ') 
    else: 
        print('dropped', end=' ') 
else: 
    print(mystr[4:26], end=' ') 
print('down') 
 #It would print out: The quick brown fox brown cow jumped over the lazy dog down. I assume that the string was a list, each index equals to a space or character
 #Correct Answer: The fox jumped down


mylist = [] 
for i in range(5): 
    mylist.append(i ** 2) 
print(mylist[-3:]) 

#It would print out: mylist = [0, 1, 4, 9, 16], print out [4, 9, 16]


mystr = "Howdy! Welcome to Texas A&M Engineering!" 
print(mystr[:5] + mystr[6] + mystr[18:] + '\b students!')

#It would print out: Howdy! Texas A&M Engineering students!


#FIRST FRQ QUESTION, DID NOT PASS
months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
monthsStr = ""

for i in range(5):
    monthsInput = input("Please enter a birthday:")
    monthsStr += monthsInput + " "
    if i == 5:
        monthsStr += monthsInput
monthsList = monthsStr.split(" ")
for i in range(0, 12, 2):
    print(monthsList[i]) 

for i in range(1, 12, 2):
    print(monthsList[i])
    

guesses = 1
wordguess = ""
letters = []
i = 0
while len(letters) < 6:
    hangman = input("Enter the secret word:")
    letters = [letter for letter in hangman]
    if len(letters) < 6:
        print("Please put a word with more than 6 characters.")
wordguess = input("Guess a letter:")
firstword = hangman



for i in range(len(letters)):
    if(wordguess in letters):
        wordguess = input("Guess another letter:")
        guesses +=1
    elif(wordguess != letters[i]):
        break


print(f"The secret word is: \"{firstword}\". You took {guesses} guesses!")


UIN = int(input("Enter a UIN:"))
UINpublish = []
information = []
roster = [[123004567], ['Joe', 'Aggie', 'ENGE', 3.50], [532001230], ["Jacob", "Hou", "ENGR", 3.75]]
for i in range(0, len(roster), 2):
    if(UIN in UINpublish):
        UINpublish = roster[i]
for j in range(1, len(roster), 2):
    information = roster[j]

print(f"{information[0]} {information[1]}: {information[2]}, {information[3]}")


letters = ["a", "b", "c", "d", "e"]
j = 1
for i in range(0, 5):
    print(str(letters[i]) * j)
    j += 1

age = 0
ages = []
while age > -1:
    if(len(ages) < 1):
        age = int(input("Enter an age: "))
    ages.append(age)
    age = int(input("Enter another age: "))
ages.sort(reverse=True)
print("Number of people Minimum age Maximum age")
print(", ".join(map(str, ages)))

phoneNumber = input("Enter a phone number in this format XXX-XXXXXXX:")
originalphoneNumber = phoneNumber
phoneList = [phone for phone in phoneNumber]
numberPhoneList = phoneList[:4]
phoneList = phoneList[4:]
print(numberPhoneList)
for i in range(0, len(phoneList)):
    if(phoneList[i] == "A"or "B" or "C"):
        phoneList[i] = "1"
finalphoneNumber = numberPhoneList + phoneList
print(finalphoneNumber)
print(f"{originalphoneNumber} is equivalent to")
"""







