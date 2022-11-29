import numpy as np

# Open the file
with open("data.dat", "r") as file:
    # Skip the first line
    file.readline()

    # Headers
    headers = file.readline().split(", ")

    # Skip again
    file.readline()

    # Create the array
    arr = []
    for line in file:
        arr.append(line.strip().split(", "))

        # Convert to floats
        for j in range(len(arr[-1])):
            arr[-1][j] = float(arr[-1][j])

    # Convert to numpy
    np_arr = np.array(arr)
    print(np_arr)
    print(np_arr.shape)