# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   Lab 10.14
# Date:         31 October 2022
#
#

#need two functions that determine if the number is higher or lower
#maybe put both try-except function?

def inputguess(guess):
    number = 26
    if guess > number:
        print("Too high!")
    if guess < number:
        print("Too low!")
    if guess == number:
        return

def validInt(guess):
    #newGuess = guess
    while True:
        try:
            guess = int(guess)
            inputguess(guess)
            #count += 1
            break
        except:
            guess = input("Bad input! Try again: ")
            continue
    return guess


print("Guess the secret number! Hint: it's an integer between 1 and 100... ")
count = 0   
while True:
    guess = input("What is your guess? ") 
    guess = validInt(guess)
    count += 1
    if guess == 26:
        break
    

print(f"You guessed it! It took you {count} guesses.")



