# Store the data
females = []
males = []

# Get input
sex = input("What is the gender (F for female, M for male): ")
age = int(input("What is the age: "))

# Main loop
while age >= 0:
    # Add to appropriate list
    if sex == "F":
        females.append(age)
    elif sex == "M":
        males.append(age)

    # Get more input
    sex = input("What is the gender (F for female, M for male): ")
    age = int(input("What is the age: "))

# Write to file
females.sort()
males.sort()

with open("Student_Data_19Sp.txt", "w") as f:
    f.write(f"{'Gender':10}Number of Students  Minimum Age  Maximum Age\n")
    f.write(f"{'Female':10}{len(females):<20}{females[0]:<13}{females[-1]}\n")
    f.write(f"{'Male':10}{len(males):<20}{males[0]:<13}{males[-1]}\n")