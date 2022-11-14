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
    if num == 5:
        asc_clock[0].append("555 ")
        asc_clock[1].append("5   ")
        asc_clock[2].append("555 ")
        asc_clock[3].append("  5 ")
        asc_clock[4].append("555 ")
    if num == 6:
        asc_clock[0].append("666 ")
        asc_clock[1].append("6   ")
        asc_clock[2].append("666 ")
        asc_clock[3].append("6 6 ")
        asc_clock[4].append("666 ")
    if num == 7:
        asc_clock[0].append("777 ")
        asc_clock[1].append("  7 ")
        asc_clock[2].append("  7 ")
        asc_clock[3].append("  7 ")
        asc_clock[4].append("  7 ")
    if num == 8:
        asc_clock[0].append("888 ")
        asc_clock[1].append("8 8 ")
        asc_clock[2].append("888 ")
        asc_clock[3].append("8 8 ")
        asc_clock[4].append("888 ")
    if num == 9:
        asc_clock[0].append("999 ")
        asc_clock[1].append("9 9 ")
        asc_clock[2].append("999 ")
        asc_clock[3].append("  9 ")
        asc_clock[4].append("999 ")

for index, value in enumerate(time):  #enumerate function turns a "dictionary" using the time as the key to get the shape as the "value"
    if value != ':':
        numbers(int(time[index]))     #if-else statement to see if the value of the input is a colon or not
    else:
        asc_clock[0].append("  ")
        asc_clock[1].append(": ")
        asc_clock[2].append("  ")
        asc_clock[3].append(": ")
        asc_clock[4].append("  ")
print()
for i in range(5):                     #prints the entire shape of the clock as ascii characters
    print(*asc_clock[i], sep ='')