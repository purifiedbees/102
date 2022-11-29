# Prompt for values
entries = int(input("Enter number of people: "))
file_name = input("Enter file name: ")

# Open file
with open(file_name, "w") as f:
    # Write the top line
    f.write(f"{'Name':<15}Score\n")

    # Helper variable
    total_grade = 0
    count = entries

    # Get input and write
    while entries > 0:
        name = input("Please enter a name: ")
        score = float(input("Please enter a score: "))

        total_grade += score

        f.write(f"{name:<15}{score}\n")

        entries -= 1

    # Average
    print(f"The average grade for this quiz is {total_grade/count:.1f}")

    



    