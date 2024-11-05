import numpy as np

array = np.random.randint(0,10000,size = 100)
print("Original Array:")
print(array)

indices = np.where(np.char.endswith(array.astype(str), '6'))

elements_ending_with_6 = array[indices]

print("Elements ending with '6':")
print(elements_ending_with_6)



