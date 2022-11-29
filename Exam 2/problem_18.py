import math

# Input
x = float(input("Enter x: "))

# The term function
def Tay_term(n: int) -> float:
    return (((-1) ** n) / math.factorial(2 * n)) * (x ** (2 * n))

# Summation loop
tolerance = 0.00001
n = 0
next_term = Tay_term(n)
summation = 0

while abs(next_term) >= tolerance:
    summation += next_term

    n += 1
    next_term = Tay_term(n)

# Output
print(f"The cosine of {x} is {summation:.4f}")