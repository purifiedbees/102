# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   12.17
# Date:         28 November 2022
#
import numpy as np
from matplotlib import pyplot as plt
import csv

AllWeather = []
dates = []
windSpeed = []
rain = [] #precipitation
avgTemp = []
maxTemp = []
minTemp = []
days = 0
with open("WeatherDataCLL.csv") as data:
    reader = csv.reader(data, delimiter = ",")
    for i in reader:
        AllWeather.append(i)
for weather in range(1, len(AllWeather)):
    dates.append(AllWeather[weather][0])
    windSpeed.append(float(AllWeather[weather][1]))
    rain.append(float(AllWeather[weather][2]))
    avgTemp.append(int(AllWeather[weather][3]))
    maxTemp.append(int(AllWeather[weather][4]))
    minTemp.append(int(AllWeather[weather][5]))
"""
#plot 1
x = dates
y1 = maxTemp
y2 = windSpeed
#gets two y-axes
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
#makes the x axis and y axes
plt.xticks(np.arange(0, len(AllWeather), 200))
ax1.plot(x, y1, color = "green")
ax2.plot(x, y2, color = "blue")
ax1.set_ylabel("Maximum Temperature, F")
ax2.set_ylabel("Average Wind Speed, mph")
plt.xlabel("Date")
plt.title("Maximum Temperature and Average Wind Speed")
ax1.legend(["Max Temp"], loc = "lower left")
ax2.legend(["Avg Wind Temp"], loc = "lower right")
plt.show()

#plot 2
x = windSpeed
plt.xlabel("Average Wind Speed, mph")
plt.ylabel("Number of days")
plt.title("Histogram of average wind speed")
plt.hist(x, bins = 30, color = green)
plt.show()


#plot 3
x = minTemp
y = windSpeed
plt.title("Average Wind Speed vs Minimum Temperature")
plt.ylabel("Average Wind Speed, mph")
plt.xlabel("Minimum Temperature, F")
plt.scatter(x, y, c = "black", s = 5)
plt.show()
"""

#plot 4

