import numpy as np

array = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        if i == j :
            array[i][i] = 1
print (array)