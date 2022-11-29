# Get and validate input
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

except:
    pass

else:
    # Swap to ensure a < b if necessary
    a, b = min(a, b), max(a, b)

    # Sum everything up
    partial_sum = 0
    for num in range(a, b+1):
        if num % 4 == 0:
            partial_sum += num

    print(partial_sum)
