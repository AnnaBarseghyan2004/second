import numpy as np

matrix1 = np.random.randint(0, 10, size=(2, 2))
matrix2 = np.random.randint(0, 10, size=(2, 2))
print(matrix1)
print(matrix2)

result = matrix1 * matrix2 
print(result)      

result1 = np.dot(matrix1,matrix2)
print(result1)