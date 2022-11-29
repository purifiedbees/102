# Get input
x = float(input("Enter x: "))

# Necessary values
TOL = 10**-6
term = 1
n = 0
summation = 0

# Summation loop
while abs(term) >= TOL:
    summation += term

    n += 1
    term = x**n

# Output
print(summation)