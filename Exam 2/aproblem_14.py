# Store data
patient_data = {}

# Get data
number_of_patients = int(input("Please enter the number of patients: "))

while number_of_patients > 0:
    name = input("Please enter the name: ")
    symptoms = input("Please enter symptoms: ")

    patient_data[name] = symptoms
    number_of_patients -= 1

# Retrieve
desired_patient = input("Please enter patient name (-1 to quit): ")
while desired_patient != "-1":
    if desired_patient not in patient_data.keys():
        print("Patient is not in our records.")
    else:
        print(patient_data[desired_patient])

    desired_patient = input("Please enter patient name (-1 to quit): ")