# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jacob Hou
#               Derick
#               Shane
#               Adan
# Section:      524
# Assignment:   Wumpus
# Date:         4 December 2022
#
import random as rand

#functions to use 
roomnumbers = [[1,4,7], [9,0,2], [11,1,3], [13,2,4], [0,5,3], [4,6,14], [16,5,7], [6,8,0], [17,7,9], [8,10,1], [18,9,11], [10,2,12], [11,13,19],
[3,12,14], [15,13,5], [14,16,19], [15,17,6], [16,18,8], [17,19,10], [18,15,12]]         #each actual room number is index + 1

wumpus = 3    #these are place holder variables
bats = [2, 4]
holes = [5, 8]

arrows = 5
pos = 0     

def shoot(path):       #shoots an arrow and checks if the path shot is an accurate one
    path.insert(0, pos)

    for i in range(1, len(path)):
        adj = roomnumbers[i-1]
        if path[i] not in adj:  #if not, it returns false and the use the randompath() to get a random path for the arrow to travel
            return False
        elif wumpus == i:
            return 'win'
    
    return True

def randompath():   #randompath for arrows if shoot(path) returns false 
    ranpath = []
    currentpos = pos
    for i in range(5):
        randomnumber = rand.randint(0,2)
        currentpos = roomnumbers[currentpos][randomnumber]
        ranpath.append(currentpos)
    return ranpath

def initialize():    #initializes the entire function and puts the wumpus and bats and holes in different positions around the game
    possiblepos = list(range(20))
    wumpus = possiblepos[rand.randint(0, len(possiblepos) - 1)]
    possiblepos.remove(wumpus)
    bats[0] = possiblepos[rand.randint(0, len(possiblepos) - 1)]
    possiblepos.remove(bats[0])
    bats[1] = possiblepos[rand.randint(0, len(possiblepos) - 1)]
    possiblepos.remove(bats[1])
    holes[0] = possiblepos[rand.randint(0, len(possiblepos) - 1)]
    possiblepos.remove(holes[0])
    holes[1] = possiblepos[rand.randint(0, len(possiblepos) - 1)]
    possiblepos.remove(holes[1])

def moving(endpos):        #lets the player move around, endpos is going to be a user inputted value
    global pos
    if endpos in roomnumbers[pos]:     #if able to move, change the room number ("pos") to the other room number ("endpos") and return true
        pos = endpos                
        return True
    else:
        return False                #if not, print out a statement saying "Sorry, you cannot move there"

def superbats():                #bats drop the player in any random room, uses the while for edge cases if the random number equals the new number get another random integer
    newpos = rand.randint(0, 19)
    while newpos == pos:
        newpos = rand.randint(0, 19)
    pos = newpos

def wakewumpus():      #wumpus if it gets to wake up, has a random chance to move or to stay in the room together
    wake = rand.randint(0,3)
    if wake != 3:
        wumpus = roomnumbers[wumpus][rand.randint(0,2)]

def show_instructions():
    print ("""
        WELCOME TO 'HUNT THE WUMPUS'
        THE WUMPUS LIVES IN A CAVE OF 20 ROOMS. EACH ROOM
        HAS 3 TUNNELS LEADING TO OTHER ROOMS.
        
    HAZARDS:
        BOTTOMLESS PITS: TWO ROOMS HAVE BOTTOMLESS PITS IN THEM
        IF YOU GO THERE, YOU FALL INTO THE PIT (& LOSE!)
        SUPER BATS: TWO OTHER ROOMS HAVE SUPER BATS. IF YOU
        GO THERE, A BAT GRABS YOU AND TAKES YOU TO SOME OTHER
        ROOM AT RANDOM, WHICH CAN BE A PIT OR WHERE THE WUMPUS IS
    WUMPUS:
        THE WUMPUS IS NOT BOTHERED BY THE HAZARDS (HE HAS SUCKER
        FEET AND IS TOO BIG FOR A BAT TO LIFT). USUALLY
        HE IS ASLEEP. TWO THINGS THAT WAKE HIM UP: YOU ENTERING
        HIS ROOM OR YOU SHOOTING AN ARROW.
        IF THE WUMPUS WAKES, HE EITHER MOVES ONE ROOM
        OR STAYS STILL. AFTER THAT, IF HE IS WHERE YOU
        ARE, HE TRAMPLES YOU (& YOU LOSE!).
    YOU:
        EACH TURN YOU MAY MOVE OR SHOOT AN ARROW
        MOVING: YOU CAN GO ONE ROOM (THRU ONE TUNNEL)
        ARROWS: YOU HAVE 5 ARROWS. YOU LOSE WHEN YOU RUN
        OUT. YOU AIM BY TELLING
        THE COMPUTER THE ROOM YOU WANT THE ARROW TO GO TO.
        IF THE ARROW HITS THE WUMPUS, YOU WIN. ARROWS CAN
        ONLY TRAVEL THROUGH 5 ROOMS UNTIL IT HITS THE GROUND.

    WARNINGS:
        WHEN YOU ARE ONE ROOM AWAY FROM WUMPUS OR A HAZARD,
        THE COMPUTER SAYS:
        WUMPUS:   'I SMELL A WUMPUS'
        BAT   :   'BATS NEAR BY'
        PIT   :   'I FEEL A DRAFT'
        """)

game = True
pos = 0 
initialize()
show_instructions()
print("You have started in room 1")
print("The Room Numbers will be from 0 to 19")
#main code
#moving loop
while game == True:
    movingstr = input("Would you like to move? (Y or N) ")
    if movingstr is ("Y" or "y"):
        endpos = int(input("Which room number would you like to move to? "))
        if moving(endpos) is True:
            print(pos)
            continue
        else:
            print("Sorry, you can't go there.")
    elif movingstr is ("N" or "n"):
        continue
    else:
        print("Sorry, I don't know what you mean by that.")
        continue
    usingArrows = input("Would you like to shoot an arrow? (Y or N) ")
    if usingArrows == "Y" or "y":
        path = input("What is your room path to shoot? (Put the room numbers in order with commas separating them) ")
        path = path.split(",")
        if len(path) > 5:
        print(path)
        break
    else:
        continue
    
    