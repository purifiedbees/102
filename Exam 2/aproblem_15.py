# Open the file
with open("grades.txt", "r") as f:
    grades = f.readlines()

    # Convert to numbers
    for i in range(len(grades)):
        grades[i] = float(grades[i])

    # Get stats
    lowest, highest = min(grades), max(grades)
    average = sum(grades) / len(grades)

    # Output
    print(f"Average score: {average}, Maximum Score: {highest}, Minimum Score: {lowest}")