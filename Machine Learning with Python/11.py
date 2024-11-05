import numpy as np

matrix = np.arange(9).reshape((3, 3))

print(matrix)

matrix[:, [0, 2]] = matrix[:, [2, 0]]

print(matrix)
