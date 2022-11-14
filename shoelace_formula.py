# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Derick Harrington
#               Jacob Hou
#               Shane Gorski
#               Adan Plata
# Section:      ENGR 524
# Assignment:   Lab 9
# Date:         24 October 2022

def getpoints(mainpoints):
    j = 0                       #using an iterator to go through each index and split the list into a lists of lists
    mainpoints = mainpoints.split()   #first split for each pair of vertices to be by itself
    for i in mainpoints:     
        mainpoints[j] = i.split(",")   #second split for each vertice in each index to be separated by commas
        j += 1
    i = 0
    for points in mainpoints:          #changes each str in the list into an int
        j = 0
        for k in points:
            mainpoints[i][j] = int(k)
            j += 1
        i += 1
    return mainpoints    

def cross(x, y):
    return(x[0] * y[1]) - (x[1] * y[0]) #cross multiplying each value
    
def shoelace(mainpoints):
    area = []
    for x in (range(len(mainpoints) - 1)): #for loop that goes 1 less than the length of the list since we are adding one to the indexes in the .append() command
        area.append((mainpoints[x][0] * mainpoints[x+1][1]) - (mainpoints[x][1] * mainpoints[x+1][0]))     
    area.append((mainpoints[-1][0] * mainpoints[0][1]) - (mainpoints[0][0] * mainpoints[-1][1]))   #since the loop goes 1 less, this gets the final vertex
    sumArea = sum(area)
    sumArea /= 2
    return sumArea
def main():
    mainpoints = input("Please enter the vertices : ")
    mainpoints = getpoints(mainpoints)
    total = shoelace(mainpoints)
    print()
    print(f"The area of the polygon is {total:.1f}")

if __name__ == '__main__':
    main()















