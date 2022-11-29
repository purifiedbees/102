def y(x: float) -> float:
    return x**3 - (3 * (x**2)) - (5.5 * x) + 25

# NOTE: this solution is not entirely accurate but is within an acceptable accuracy

# Constants
LOWER_LIMIT, UPPER_LIMIT = -3, 5
current_x = LOWER_LIMIT
step = 0.00001

while current_x <= UPPER_LIMIT:
    left, current, right = y(current_x - step), y(current_x), y(current_x + step)

    # Local maxima
    if left < current and right < current:
        print(f"({current_x}, {current})")
    # Local minima
    if left > current and right > current:
        print(f"({current_x}, {current})")

    current_x += step