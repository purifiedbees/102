# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jacob Hou
# Section:      524
# Assignment:   11.11
# Date:         8 November 2022
#


def barcode_firsthalf(barcodes):
    barcode_firsthalflist = []
    barcode_secondhalflist = []
    barcode_list = []
    barcode_list = list(map(int, barcodes))  #map() returns the list as the values 
    for barcode in range(len(barcode_list)-1):
        if barcode % 2 != 0:
            barcode_firsthalflist.append(barcode_list[barcode])
        else:
            barcode_secondhalflist.append(barcode_list[barcode])

    return barcode_firsthalflist, barcode_secondhalflist #gets the even numbers, need each number in a "even" spot
    #don't forget to pop last number off


counter = 0
file = open(input("Enter the name of the file: "))
barcodes = file.readlines()
validfile = open("validfile.txt", "w")
for barcode in barcodes:
    barcode = barcode[:-1]
    a, b = barcode_firsthalf(barcode)
    barcode_secondhalfsum = sum(b)
    barcode_firsthalfsum = sum(a)
    barcode_product = barcode_firsthalfsum * 3
    barcode_sum = barcode_product + barcode_secondhalfsum
    barcode_sumstr = str(barcode_sum) # or modulus 
    #change to string to get the last digit of the number
    last_digit = barcode_sumstr[-1]
    last_digit = int(last_digit)
    #check the validity of the number
    valid = 10 - last_digit
    if valid == int(barcode[-1]):
        validfile.write(barcode)
        validfile.write("\n")
        counter += 1

print(f"There are {counter} valid barcodes")
file.close()
validfile.close()
