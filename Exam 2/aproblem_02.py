# Loop and get inputs
numbers = []
duplicates_found = False

while len(numbers) < 5:
    n = int(input("Enter a number: "))

    # Check for duplicates
    if n in numbers:
        duplicates_found = True

    numbers.append(n)

# Output
if duplicates_found:
    print("Duplicates")
else:
    print("All Unique")