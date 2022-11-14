# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:
# Section:      524
# Assignment:   Lab 7
# Date:         10/12/22



print("At any point to stop playing, type stop for the letter and number of the coordinate.")
game1 = input("Enter @, O, or # as player 1 gamepiece:") #takes input for the gamepieces
game2 = input("Enter player 2 gamepiece:")

t = 1



rows = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"] #basic layout of gameboard that will be changed
rowA = ["A", ".", ".", ".", ".", ".", ".", ".", ".", "."]
rowB = ["B", ".", ".", ".", ".", ".", ".", ".", ".", "."]
rowC = ["C", ".", ".", ".", ".", ".", ".", ".", ".", "."]
rowD = ["D", ".", ".", ".", ".", ".", ".", ".", ".", "."]
rowE = ["E", ".", ".", ".", ".", ".", ".", ".", ".", "."]
rowF = ["F", ".", ".", ".", ".", ".", ".", ".", ".", "."]
rowG = ["G", ".", ".", ".", ".", ".", ".", ".", ".", "."]
rowH = ["H", ".", ".", ".", ".", ".", ".", ".", ".", "."]
rowI = ["I", ".", ".", ".", ".", ".", ".", ".", ".", "."]


print(*rows, sep=" ") #prints rows without brackets
print(*rowA, sep=" ")
print(*rowB, sep=" ")
print(*rowC, sep=" ")
print(*rowD, sep=" ")
print(*rowE, sep=" ")
print(*rowF, sep=" ")
print(*rowG, sep=" ")
print(*rowH, sep=" ")
print(*rowI, sep=" ")

while t == 1: #keeps program repeating until stop is typed and the program breaks

    notDone = True
    while notDone:
        print("Player 1's turn")
        placeLET = input("Enter letter of coordinate:")
        placeNUM = input("Enter number of coordinate:")
        if ((placeLET == "stop") and (placeNUM == "stop")) or ((placeLET == "Stop") and (placeNUM == "Stop")):
            break
        else:
            placeNUM = int(placeNUM)

        if (placeLET == "A") or (placeLET == "a"): #if else statement to find out which element to change
            for i in range(1,10):
                if (placeNUM == i) and (rowA[i] == "."):
                    rowA[i] = game1 #changes spot to gamepiece
                    notDone = False
                elif (placeNUM == i) and (rowA[i] != "."):
                    print("This space is not open.")

        elif (placeLET == "B") or (placeLET == "b"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowB[i] == "."):
                    rowB[i] = game1
                    notDone = False
                elif (placeNUM == i) and (rowB[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "C") or (placeLET == "c"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowC[i] == "."):
                    rowC[i] = game1
                    notDone = False
                elif (placeNUM == i) and (rowC[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "D") or (placeLET == "d"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowD[i] == "."):
                    rowD[i] = game1
                    notDone = False
                elif (placeNUM == i) and (rowD[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "E") or (placeLET == "e"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowE[i] == "."):
                    rowE[i] = game1
                    notDone = False
                elif (placeNUM == i) and (rowE[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "F") or (placeLET == "f"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowF[i] == "."):
                    rowF[i] = game1
                    notDone = False
                elif (placeNUM == i) and (rowF[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "G") or (placeLET == "g"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowG[i] == "."):
                    rowG[i] = game1
                    notDone = False
                elif (placeNUM == i) and (rowG[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "H") or (placeLET == "h"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowH[i] == "."):
                    rowH[i] = game1
                    notDone = False
                elif (placeNUM == i) and (rowH[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "I") or (placeLET == "i"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowI[i] == "."):
                    rowI[i] = game1
                    notDone = False
                elif (placeNUM == i) and (rowI[i] != "."):
                    print("This space is not open.")
        else:
            print("Invalid Input")

    if ((placeLET == "stop") and (placeNUM == "stop")) or ((placeLET == "Stop") and (placeNUM == "Stop")):
        break
    print(*rows, sep=" ")
    print(*rowA, sep=" ")
    print(*rowB, sep=" ")
    print(*rowC, sep=" ")
    print(*rowD, sep=" ")
    print(*rowE, sep=" ")
    print(*rowF, sep=" ")
    print(*rowG, sep=" ")
    print(*rowH, sep=" ")
    print(*rowI, sep=" ")


    notDone = True
    while notDone:
        print("Player 2's turn")  # same thing for player 2
        placeLET = input("Enter letter of coordinate:")
        placeNUM = input("Enter number of coordinate:")

        if (placeLET == "stop") or (placeLET == "Stop"):
            break
        else:
            placeNUM = int(placeNUM)

        if (placeLET == "A") or (placeLET == "a"):
            for i in range(1,10):
                if (placeNUM == i) and (rowA[i] == "."):
                    rowA[i] = game2
                    notDone = False
                elif (placeNUM == i) and (rowA[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "B") or (placeLET == "b"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowB[i] == "."):
                    rowB[i] = game2
                    notDone = False
                elif (placeNUM == i) and (rowB[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "C") or (placeLET == "c"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowC[i] == "."):
                    rowC[i] = game2
                    notDone = False
                elif (placeNUM == i) and (rowC[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "D") or (placeLET == "d"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowD[i] == "."):
                    rowD[i] = game2
                    notDone = False
                elif (placeNUM == i) and (rowD[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "E") or (placeLET == "e"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowE[i] == "."):
                    rowE[i] = game2
                    notDone = False
                elif (placeNUM == i) and (rowE[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "F") or (placeLET == "f"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowF[i] == "."):
                    rowF[i] = game2
                    notDone = False
                elif (placeNUM == i) and (rowF[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "G") or (placeLET == "g"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowG[i] == "."):
                    rowG[i] = game2
                    notDone = False
                elif (placeNUM == i) and (rowG[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "H") or (placeLET == "h"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowH[i] == "."):
                    rowH[i] = game2
                    notDone = False
                elif (placeNUM == i) and (rowH[i] != "."):
                    print("This space is not open.")
        elif (placeLET == "I") or (placeLET == "i"):
            for i in range(1, 10):
                if (placeNUM == i) and (rowI[i] == "."):
                    rowI[i] = game2
                    notDone = False
                elif (placeNUM == i) and (rowI[i] != "."):
                    print("This space is not open.")
        else:
            print("Invalid Input")

    if ((placeLET == "stop") and (placeNUM == "stop")) or ((placeLET == "Stop") and (placeNUM == "Stop")):
        break
    print(*rows, sep=" ")
    print(*rowA, sep=" ")
    print(*rowB, sep=" ")
    print(*rowC, sep=" ")
    print(*rowD, sep=" ")
    print(*rowE, sep=" ")
    print(*rowF, sep=" ")
    print(*rowG, sep=" ")
    print(*rowH, sep=" ")
    print(*rowI, sep=" ")

print("Thanks for playing dawg")

