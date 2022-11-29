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
    for i in range(4):
        arr.append(file.readline().strip().split(", "))
        
        # Convert to floating point
        for j in range(len(arr[i])):
            arr[i][j] = float(arr[i][j])

    # Convert to numpy
    np_arr = np.array(arr)
    print(np_arr)
    print(np_arr.shape)