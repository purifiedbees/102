# Implement the equation
def y(x: int) -> float:
    return (x**3) - (2.1* x**2) + (14*x) - 5

# Area function
def area_calculator(a: float, b: float) -> float:
    # Integration 
    step = (b - a) / 200
    summation = 0
    left = a

    while left < b:
        # Interval mid strategy
        right = left + step
        mid = (left + right) / 2
        area = step * y(mid)

        summation += area
        left = right

    return summation

# Grab input
a, b = 1, 0

while not b > a:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

# Output
print(f"The area between {a} and {b} is {area_calculator(a, b)}")