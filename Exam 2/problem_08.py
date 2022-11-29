# Helper function

def get_divisors(N: int) -> list[int]:
    divisors = [1]

    # Do the main loop
    lower, upper = 2, N
    while lower < upper:
        # New divisors found
        if N % lower == 0:
            upper = N // lower
            divisors.append(lower)
            divisors.append(upper)

        lower += 1

    return divisors

def is_perfect(N: int) -> bool:
    # Edge case
    if N == 1:
        return False

    divisors = get_divisors(N)

    return sum(divisors) == N

# Example to test functions with
print(is_perfect(6), sorted(get_divisors(6)))
print(is_perfect(28), sorted(get_divisors(28)))
print(is_perfect(8), sorted(get_divisors(8)))
print(is_perfect(27), sorted(get_divisors(27)))