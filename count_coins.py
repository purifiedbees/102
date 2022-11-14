# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   11.12
# Date:         8 November 2022
#

def command(game):
    line_list = []
    coin = 0
    index = 0
    coin_changes = []
    for line in game:
        line = line.split()
        line_list.append(line)
        
    while index != 650:
#while loop, store the index of what line the code is on, if it's on the last line break, create outside variable "coin", add that to coin/jump/none
        if line_list[index][0] == "jump":
            index += int(line_list[index][1])
        elif line_list[index][0] == "coin":
            coin += int(line_list[index][1])
            coin_changes.append(int(line_list[index][1]))
            index += 1
        else:
            index += 1
    return coin, coin_changes #returns the total amount of coins, need to find a way to display each value of coins before the very end

with open("game.txt") as game:
    file = open("game.txt")
    game = file.readlines()
with open("coins.txt", "w") as coins:
    gameline = command(game)
    for coin in gameline[1]:
        coins.write(str(coin) + "\n")

print(f"Total coins collected: {gameline[0]}")

