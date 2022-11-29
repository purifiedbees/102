import numpy as np

# Helper function

def matrix_mult(A: np.array, B: np.array) -> np.array:
    # Personal usage, this just me telling y'all that A and B are guarenteed able to be multiplied together
    assert(A.shape[1] == B.shape[0])

    # The actual calculation
    return np.matmul(A, B)

def long_way(A: np.array, B: np.array) -> np.array:
    result = []

    # Each row of A...
    new_row = []
    for row in range(A.shape[0]):
        # Each column of B...
        for col in range(B.shape[1]):
            # Each element in the row of A and col of B...
            row_result = 0
            for i in range(A.shape[1]):
                row_result += A[row, i] * B[i, col]
            new_row.append(row_result)
        
        # Update the resultant matrix
        result.append(new_row)
        new_row = []

    return np.array(result)

# Example to test
A = np.array([[3, 5], [3, 4], [9, 1]])
B = np.array([[3, 4, 3], [5, 6, 5]])

print(matrix_mult(A, B))
print(long_way(A, B))

"""
Using A @ B works but the above two solutions are for people who are more familiar with those approaches.
"""