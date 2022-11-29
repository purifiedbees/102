# Helper functions

def mean(nums: list[float]) -> float:
    return sum(nums) / len(nums)

def variance(nums: list[float]) -> float:
    m = mean(nums)

    # Summation loop
    summation = 0
    for num in nums:
        summation += (num - m) ** 2

    # Calculation
    return summation / len(nums)    # Standard deviation would be sqrt of this result

# Input
numbers = input("Enter a list of numbers separated by commas: ").split(",")

# Clean up the input
for i in range(len(numbers)):
    numbers[i] = float(numbers[i].strip())

# Output
print(f"Mean: {mean(numbers)}, Variance: {variance(numbers)}")