# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Derick Harrington
#               Jacob Chou
#               Adan Plata
#               Shane Gorski
# Section:      524
# Assignment:   Module 13 Lab
# Date:         12/5/2022

import turtle as turt

print("Instructions for the game:\nPlayer 1 is blue, and Player 2 is green,"   #simple game instructions
" whichever player connects four of their colored pieces in a row first wins! \nBe sure to not cheat and move for your opponent!")

def dcircle(x, y, rad, color):   #function for each the shape of the pieces
    turt.up()
    turt.goto(x, y - rad)
    turt.seth(0)
    turt.down()
    turt.fillcolor(color)
    turt.begin_fill()
    turt.circle(rad, 360, 100)
    turt.end_fill()

def drboard(x, y, len, hei, color): #function for the shape of the board
    turt.up()
    turt.goto(x, y)
    turt.seth(0)
    turt.down()
    turt.fillcolor(color)
    turt.begin_fill()
    turt.fd(len)
    turt.left(90)
    turt.fd(hei)
    turt.left(90)
    turt.fd(len)
    turt.left(90)
    turt.fd(hei)
    turt.left(90)
    turt.end_fill()


screen = turt.Screen()
screen.setup(600, 600)       #size of the board
screen.setworldcoordinates(-450, -500, 450, 500)
screen.tracer(0, 0)
score = turt.Turtle()
r1 = 6   #connect 4 uses 6 rows and 7 columns
c1 = 7
xaxis = -400      #how big the board is one screen
yaxis = -400 * r1 / c1
l1 = -2 * xaxis
h1 = -2 * yaxis

def dpieces():
    global board
    rgap = h1 / r1
    cgap = l1 / c1
    Y = yaxis + rgap / 2
    for i in range(r1):
        X = xaxis + cgap / 2
        for j in range(c1):
            if board[i][j] == 0:
                dcircle(X, Y, rgap / 3, 'white')
            elif board[i][j] == 1:
                dcircle(X, Y, rgap / 3, 'blue')
            else:
                dcircle(X, Y, rgap / 3, 'green')
            X += cgap
        Y += rgap

def dboard():   #draws board as 400 by 400 in black
    drboard(xaxis, yaxis, l1, h1, 'black')

def draw():
    dboard()
    dpieces()
    screen.update()  #keeps up with the board

def main_game(piec, turn, r, d):
    val = 1  #if board has a horizontal or vertical conenct 4
    i = d + 1
    while i < c1 and piec[r][i] == turn: val, i = val + 1, i + 1
    i = d - 1
    while i >= 0 and piec[r][i] == turn: val, i = val + 1, i - 1
    if val >= 4: return turn
    if r >= 3 and piec[r - 1][d] == turn and piec[r - 2][d] == turn and piec[r - 3][d] == turn: return turn

    val = 1   #if board has a diagonal connect 4
    i = 1
    while r + i < r1 and d + i < c1 and piec[r + i][d + i] == turn: val, i = val + 1, i + 1
    i = -1
    while r + i >= 0 and d + i >= 0 and piec[r + i][d + i] == turn: val, i = val + 1, i - 1
    if val >= 4: return turn
    val = 1
    i = 1
    while r + i < r1 and d - i >= 0 and piec[r + i][d - i] == turn: val, i = val + 1, i + 1
    i = -1
    while r + i >= 0 and d - i < c1 and piec[r + i][d - i] == turn: val, i = val + 1, i - 1
    if val >= 4: return turn
    for i in range(c1):
        if piec[r1 - 1][i] == 0:
            return -2
    return 0

def piece_on_board(piec, turn, col):   #function that places piece in the correct column per turn
    for i in range(r1):
        if piec[i][col] == 0:
            piec[i][col] = turn
            return i

def big_board():
    global board
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(0)
        board.append(row)

def bigpp(piec, turn, colum):  #piece colors and screen updates
    rowz = piece_on_board(piec, turn, colum)
    rgap = h1 / r1
    cgap = l1 / c1
    Y = yaxis + rgap * rowz + rgap / 2
    X = xaxis + cgap * colum + cgap / 2
    i = rowz
    j = colum
    if board[i][j] == 0:
        dcircle(X, Y, rgap / 3, 'white')
    elif board[i][j] == 1:
        for k in range(5):
            dcircle(X, Y, rgap / 3, 'white')
            screen.update()
            dcircle(X, Y, rgap / 3, 'blue')
            screen.update()
    else:
        for k in range(5):
            dcircle(X, Y, rgap / 3, 'white')
            screen.update()
            dcircle(X, Y, rgap / 3, 'green')
            screen.update()
    return rowz

def play(x,y):     #function for end results
    global turn,working
    if working: return
    working = True
    cols = [ 900/7*i-450+900/14 for i in range(7) ]
    for i in range(len(cols)):
        if abs(x-cols[i]) < 900/14*2/3 and board[r1-1][i]==0:
            rn = bigpp(board,turn,i)
            r = main_game(board,turn,rn,i)
            if r==0:
                screen.textinput('Game over',"It's a draw!")
            elif r==1:
                screen.textinput('Game Over','Player 1 wins!')
            elif r==-1:
                screen.textinput('Game Over','Player 2 wins!')
            if r!=-2: screen.bye()
            turn = -turn
    working = False

board = []
big_board()
dboard()
dpieces()
turn = 1
working = False
screen.onclick(play)  #found out you can interact on the board using clicks
screen.mainloop()     #keeps the board out to keep playing