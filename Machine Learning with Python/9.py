import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7], [8]])
result = np.hstack((array1,array2))

print (result)