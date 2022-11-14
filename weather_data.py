# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   11.13
# Date:         13 November 2022
#

import csv
AllWeather = []
dates = []
windSpeed = []
rain = [] #precipitation
avgTemp = []
maxTemp = []
minTemp = []
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

#getting absolute max temp
absMaxTemp = int(maxTemp[0])
for temp in maxTemp:
    if int(absMaxTemp) < int(temp):
        absMaxTemp = temp
#getting absolute min temp
absMinTemp = int(minTemp[0])
for temp in minTemp:
    if int(absMinTemp) > int(temp):
        absMinTemp = temp
#getting avg precipation
avgRain = sum(rain) / len(rain)

print(f"3-year maximum temperature: {absMaxTemp} F")
print(f"3-year minimum temperature: {absMinTemp} F")
print(f"3-year average precipitation: {avgRain:.3f} inches")

month = input("Please enter a month: ")
year = input("Please enter a year: ")
print(f"For {month} {year}: ")
monthNums = {"January":"1/", "February":"2/", "March":"3/", "April":"4/", "May":"5/", "June":"6/", 
"July":"7/", "August":"8/", "September":"9/", "October":"10", "November":"11", "December":"12"}
monthNum = monthNums[month]

validDays = []
avgMaxTemp = 0
dayRain = 0
avgWindSpeed = 0
days = 0
i = 0
#find valid dates of month and year
for date in dates:
    if date[:2] == monthNum and date[-4:] == year:
        validDays.append(i)
        days += 1
    i += 1
#finds the days with rain, gets max temp, gets wind speed
for index in validDays:
    avgMaxTemp += maxTemp[index]
    avgWindSpeed += windSpeed[index]
    if rain[index] != 0:
        dayRain += 1
avgMaxTemp /= days
avgWindSpeed /= days
dayRain = (dayRain / days) * 100

print(f"Mean maximum daily temperature: {avgMaxTemp:.1f} F")
print(f"Mean daily wind speed: {avgWindSpeed:.2f} mph")
print(f"Percentage of days with precipitation: {dayRain:.1f} %")