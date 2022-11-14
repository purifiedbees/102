# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Derick Harrington
#               Jacob
#               Shane
#               Adan
# Section:      ENGR 524
# Assignment:   Lab 8
# Date:         24 October 2022




asc_clock = [[],[],[],[],[]]      #empty list to grab each 1/5 "part" of the code
time = input("Enter the time: ")

def numbers(num): #function to grab the number shape through an if-else statement
    if num == 0:
        asc_clock[0].append("000 ")
        asc_clock[1].append("0 0 ")
        asc_clock[2].append("0 0 ")
        asc_clock[3].append("0 0 ")
        asc_clock[4].append("000 ")
    if num == 1:
        asc_clock[0].append(" 1  ")
        asc_clock[1].append("11  ")
        asc_clock[2].append(" 1  ")
        asc_clock[3].append(" 1  ")
        asc_clock[4].append("111 ")
    if num == 2:
        asc_clock[0].append("222 ")
        asc_clock[1].append("  2 ")
        asc_clock[2].append("222 ")
        asc_clock[3].append("2   ")
        asc_clock[4].append("222 ")
    if num == 3:
        asc_clock[0].append("333 ")
        asc_clock[1].append("  3 ")
        asc_clock[2].append("333 ")
        asc_clock[3].append("  3 ")
        asc_clock[4].append("333 ")
    if num == 4:
        asc_clock[0].append("4 4 ")
        asc_clock[1].append("4 4 ")
        asc_clock[2].append("444 ")
        asc_clock[3].append("  4 ")
        asc_clock[4].append("  4 ")
