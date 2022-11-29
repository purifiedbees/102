# Helper function
def is_armstrong(n: int) -> bool:
    # Extract the digits
    digits = list(str(n))

    # Cube each digit
    for i in range(len(digits)):
        digits[i] = int(digits[i]) ** 3

    # Check if sum equals n
    return sum(digits) == n

def Armstrong_number(left: int, right: int):
    # Ensure left < right
    if left > right:
        left, right = right, left

    # Generate the numbers
    numbers = []

    for num in range(left, right + 1):
        numbers.append(num)

    # Eliminate all non Armstrong numbers
    for i in range(len(numbers)-1, -1, -1):
        if not is_armstrong(numbers[i]):
            numbers.pop(i)

    # Return values
    return numbers, len(numbers) != 0