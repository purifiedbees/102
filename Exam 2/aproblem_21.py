# List of numbers
numbers = [n for n in range(1, 11, 2)]

# Helper function
def insert(n: int, numbers: list[int]) -> list[int]:
    index = 0

    # Find the index
    while index < len(numbers) and numbers[index] < n:
        index += 1

    # Insert at the index
    numbers.insert(index, n)

    return numbers

# Ask for a number
number = int(input("Enter a number: "))

# Go through and insert
insert(number, numbers)
print(numbers)