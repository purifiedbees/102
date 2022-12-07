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
    del path[0]
    return True

def randompath():   #randompath for arrows if shoot(path) returns false 
    ranpath = []
    currentpos = pos
    for i in range(5):
        randomnumber = rand.randint(0,2)
        currentpos = roomnumbers[currentpos][randomnumber]
        ranpath.append(currentpos)
    if wumpus == i:
            return 'win'
    return ranpath

def initialize():    #initializes the entire function and puts the wumpus and bats and holes in different positions around the game
    possiblepos = list(range(1, 20))
    wumpus = possiblepos[rand.randint(1, len(possiblepos) - 1)]
    possiblepos.remove(wumpus)
    bats[0] = possiblepos[rand.randint(1, len(possiblepos) - 1)]
    possiblepos.remove(bats[0])
    bats[1] = possiblepos[rand.randint(1, len(possiblepos) - 1)]
    possiblepos.remove(bats[1])
    holes[0] = possiblepos[rand.randint(1, len(possiblepos) - 1)]
    possiblepos.remove(holes[0])
    holes[1] = possiblepos[rand.randint(1, len(possiblepos) - 1)]
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
    global wumpus
    wake = rand.randint(0,3)
    if wake != 3:
        wumpus = roomnumbers[wumpus][rand.randint(0,2)]
        print("The wumpus has moved into a different room!")

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
        WUMPUS:   'YOU SMELL A WUMPUS'
        BAT   :   'THERE ARE BATS NEAR BY'
        PIT   :   'YOU FEEL A DRAFT'
        """)

game = True
pos = rand.randint(0, 20) 
winorloss = "Loss"
diecounter = 0
shotarrow = False
metwumpus = False
initialize()
show_instructions()
print(f"You have started in Room {pos}.")
print("The Room Numbers will be from 0 to 19.")
#main code
#moving loop
while game == True:
    print(f"You have {arrows} arrows left.")
    if shotarrow == True or metwumpus == True:
        wakewumpus()
    
    #conditionals for the wumpus and game
    if wumpus == roomnumbers[pos]:
        print("You smell a wumpus nearby.")
    elif bats[0] == roomnumbers[pos] or bats[1] == roomnumbers[pos]:
        print("There are bats nearby.")
    elif holes[0]  == roomnumbers[pos] or holes[1] == roomnumbers[pos]:
        print("You feel a draft.")
    else:
        pass
    #conditionals for wumpus and bats moving the player around
    if wumpus == pos:
        if shotarrow == False:
            print("You stumbled upon the wumpus! It has awaken!")
            metwumpus = True
        wakewumpus()
        diecounter += 1
        if diecounter > 1:
            print("You have been trampled by the wumpus.")
            break
    #conditionals for bats picking you up
    if bats[0] == pos or bats[1] == pos:
        print("You ventured into where one of the bats were! You got picked up and flown to a random room!")
        superbats()
        print(f"You are in Room {pos}.")
    #moving code
    print(f"There are tunnels that lead to {roomnumbers[pos]}.")
    movingstr = input("Would you like to move? (Y or N) ")
    if movingstr == ("Y"):
        endpos = int(input("Which room number would you like to move to? "))
        if moving(endpos) == True:  
            print(f"You moved to Room {pos}.")
            pass
        else:
            print("Sorry, you can't go there.")
            pass
    elif movingstr == ("N"):
        pass
    else:
        print("Sorry, I don't know what you mean by that.")
        continue
    #shooting arrows code
    usingArrows = input("Would you like to shoot an arrow? (Y or N) ")
    if usingArrows == ("Y" or "y"):
        pathstr = input("What is your room path to shoot? (Put the room numbers in order with commas separating them) ")
        arrows -= 1
        print("You used one arrow to shoot.")
        pathstr = pathstr.split(",")
        path = [eval(i) for i in pathstr]
        wakewumpus()
        shotarrow = True
        print("The Wumpus has awaken! BEWARE!")
        if len(path) < 5:
            shoot(path)
            pathstr = ", ".join(map(str, path))
            print(f"Your adventurer shoot the arrow towards rooms {pathstr}.")
        elif len(path) >= 5 or shoot(path) == False:
            print("Sorry your adventurer does not have the skill to shoot that. Your adventurer shot an arrow into the darkness instead.")
            shoot(path)
            randompath()
            if randompath() != 'win':
                ranpathstr = ", ".join(map(str, randompath()))
                print(f"Your arrow went through rooms {ranpathstr}.")
                pass
            if randompath() == 'win':
                winorloss = "Win"
                game = False
                break
    else:
        pass

    if arrows == 0 or arrows < 0:
        break
    elif wumpus == pos or holes == pos:
        break
    continue        #restarts the loop until the player wins or loses

if winorloss == "Win":
    print("You won as you killed the Wumpus! Congrats! :)")
elif winorloss == "Loss":
    print("You lost. :(")