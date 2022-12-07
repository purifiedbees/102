# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   Lab 12.17
# Date:         28 November 2022

import numpy as np
import matplotlib.pyplot as plt

#variables and lists to store data

w_d = open("WeatherDataCll.csv",'r')
temphi = []
templo = []
wind = []
data = []
for i in w_d:
    data.append(i.split(','))
data.remove(data[0])
day = len(data)
for i in data:
    wind.append(float(i[1]))
    temphi.append(float(i[4]))
    templo.append(float(i[5]))
fig, ((plot1,plot2),(plot3,plot4)) = plt.subplots(2,2,figsize=(17,12))

#Graph 1

d1 = np.linspace(1,day,1096)
pl1, = plot1.plot(d1,temphi,color = 'r',label= 'Max Temperature')
plot1.set_ylabel("Maximum temp, F")
plot1_2 = plot1.twinx()
pl2, = plot1_2.plot(d1,wind,color = 'b',label= 'Avg Wind')
plot1_2.set_ylabel("Average Wind Speed, mph")
plot1.set_yticks(np.arange(0,101,20))
plot1_2.set_yticks(np.arange(0,20.1,2.5))
plot1.set_title("Maximum Temp and Average Wind Speed")
plot1.legend(handles = [pl1,pl2],loc='lower left')

#Graph 2

x1 = np.linspace(0.0,20,30)
plot2.hist(wind,x1,edgecolor = 'k',color = 'g')
plot2.set_xlabel("Average wind speed, mph")
plot2.set_ylabel("Days")
plot2.set_title("Histogram of avg wind speed")

#Graph 3

plot3.scatter(templo,wind,color = 'k')
plot3.set_xlabel("Min Temperature, F")
plot3.set_ylabel("Avg wind speed, mph")
plot3.set_title("Avg wind speed vs min temperature")

#Graph 4

monthavg = []
monthhi = []
monthlo = []
month = 1
while month <= 12:
    month_x = []
    lTemp = 1000
    hTemp = -1000
    avgTemp = 0.0
    day = 0.0
    for i in data:
        info = i[0].split('/')
        if int(info[0]) == month:
            day += 1
            avgTemp += int(i[3])
            if int(i[4]) > hTemp:
                hTemp = int(i[4])
            if int(i[5]) < lTemp:
                lTemp = int(i[5])
    monthavg.append(avgTemp/day)
    monthhi.append(hTemp)
    monthlo.append(lTemp)
    month +=1
m_month = np.linspace(1,12,12)
pl1, = plot4.plot(m_month,monthhi,color = 'r',label = 'Highest Temperature')
pl2, = plot4.plot(m_month,monthlo,color = 'b',label = 'Lowest Temperature')
plot4.bar(m_month,monthavg,color='y')
plot4.set_xlabel("Month")
plot4.set_ylabel("Average Temperature, F")
plot4.set_title("Temperature by Month")
plot4.set_xticks(ticks = [1,2,3,4,5,6,7,8,9,10,11,12], label = [1,2,3,4,5,6,7,8,9,10,11,12])
plot4.legend(handles = [pl1,pl2],loc = 'upper left')