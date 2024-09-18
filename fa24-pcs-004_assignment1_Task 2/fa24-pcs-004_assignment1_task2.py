import numpy as np

A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
z = np.array([1, 0, 1])
b = A[:2, :2]

C = np.empty_like(A)

for i in range(A.shape[0]):
    C[i] = A[i] + z[i]

X = np.array([[1, 2],
              [3, 4]])
Y = np.array([[5, 6],
              [7, 8]])
v = np.array([9, 10])

addition_result = X + Y
print("Addition of X and Y:\n", addition_result)

multiplication_result = X @ Y
print("Multiplication of X and Y:\n", multiplication_result)

sqrt_Y = np.sqrt(Y)
print("Element-wise square root of Y:\n", sqrt_Y)

dot_product = X @ v
print("Dot product of X and v:\n", dot_product)

column_sum = np.sum(X, axis=0)
print("Sum of each column of X:\n", column_sum)
