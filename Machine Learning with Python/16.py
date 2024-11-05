import numpy as np

array = np.random.randint(1,30,size = 18)
matrix = np.reshape(array, (6,3))
print (array)
print (matrix)

indices = np.where(matrix >= 15)

elements = matrix[indices]
print (elements)