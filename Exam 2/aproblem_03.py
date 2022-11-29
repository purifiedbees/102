# Store people
people = {}

# Get input
age = int(input("Enter age: "))
name = input("Enter name: ")

# Get more input
while age != 0:
    people[age] = name

    age = int(input("Enter age: "))
    name = input("Enter name: ")

# Find names and averages
ages = sorted(list(people.keys()))

# No data is given
if len(ages) == 0:
    print("Not enough information")

else:
    # Find ages and average
    oldest_age = ages[-1]
    youngest_age = ages[0]
    average = sum(ages) / len(ages)

    # Output
    print(f"Oldest: {people[oldest_age]}, Youngest: {people[youngest_age]}, Average: {average}")