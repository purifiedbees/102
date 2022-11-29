# Take in dollars
money = input("Enter how much change you need: ")

# Split and convert to cents
dollars, cents = money.split(".")
cents = int(dollars) * 100 + int(cents)

# Calculate change
change = [0, 0, 0, 0, 0]
denominations = [100, 25, 10, 5, 1]

for i in range(len(denominations)):
    change[i] = cents // denominations[i]
    cents %= denominations[i]

print(f"Dollars: {change[0]}, Quarters: {change[1]}, Dimes: {change[2]}, Nickels: {change[3]}, Pennies: {change[4]}")

"""
// - integer division (so it removes the remainder)
% - modulus

I want to find how many whole dollars/quarters/etc -> this is with integer division
137 // 100 -> 1 dollar
137 % 100 -> 37 cents remaining

rinse and repeat for every other cent value
"""