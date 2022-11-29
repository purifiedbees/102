from ENGR102 import isprime

# Take inputs
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Ensure numbers are in the right order
if lower > upper:
    lower, upper = upper, lower

# Loop
primes = []
for num in range(lower, upper + 1):
    if num % 2 == 1 and isprime(num):
        primes.append(num)

# Output
if len(primes) == 0:
    print("No prime numbers were found")
else:
    print(primes)