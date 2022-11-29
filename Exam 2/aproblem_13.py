"""
For a polynomial ax^n1 + bx^n2 + ... + zx^0, the coefficients are a, b, ..., z
"""
coefficients = input("Enter coefficients separated by a space: ").split(" ")

# Helper function
def pad(n: int, exponent: int, degree: int) -> str:
    # Term doesn't exist
    if n == 0:
        return ""

    current_string = f"{abs(n)}x^{exponent}"

    # Don't show coefficient if n is 1 or -1 and exponent is not 0
    if abs(n) == 1 and exponent > 0:
        current_string = f"x^{exponent}"

    # Sign padding for non highest order terms
    extra_pad = " "
    if exponent == degree:
        extra_pad = ""

    # Append the sign if abs(n) != 1
    if n > 0:
        # Don't add the plus sign for the highest order term
        plus_sign = "+" if exponent != degree else ""
        current_string = f"{extra_pad}{plus_sign}{extra_pad}{current_string}"

    if n < 0:
        current_string = f"{extra_pad}-{extra_pad}{current_string}"

    # Exponent is 1
    if exponent == 1:
        current_string = current_string.split("^")[0]

    # Exponent is 0
    if exponent == 0:
        current_string = current_string.split("^")[0][:-1]

    return current_string

# Equation printer function
def form_equation(coefficients: list[str]) -> None:
    current_exponent = len(coefficients) - 1
    for coefficient in coefficients:
        print(pad(int(coefficient), current_exponent, len(coefficients)-1), end="")
        current_exponent -= 1

    # Buffer
    print()

# Derivative function
def derivative_former(coefficients: list[str]) -> None:
    # Reverse list so now index of each coefficient is equal to the degree of the term
    coefficients = coefficients[::-1]

    # Derivative
    for i in range(len(coefficients)):
        coefficients[i] = str(int(coefficients[i]) * i)

    # Reverse and remove the extra value
    coefficients = coefficients[::-1]
    coefficients.pop()

    # Output derivative
    form_equation(coefficients)

# Output
form_equation(coefficients)
derivative_former(coefficients)    


"""
input -> 1 2 3

coefficients = [1, 2, 3]

reverse of coefficients = [3, 2, 1]

equation: 1x^2 + 2x^1 + 3x^0
derivative: 2x + 2

dertivative_former(coefficients) -> (after reversal), we get [0, 2, 2]
"""