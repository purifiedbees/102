# Yield function
def percent_yield(actual: float, expected: float) -> float:
    return f"{100 * actual / expected}%\n"

# Write to file
def write_to_file(percent: str) -> None:
    with open("yields.txt", "a") as f:
        f.write(percent)

# Output
expected = float(input("Enter the ideal value: "))
actual = float(input("Enter the actual value: "))

write_to_file(percent_yield(actual, expected))