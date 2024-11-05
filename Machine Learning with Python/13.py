import numpy as np

array_10x10 = np.random.randint(0, 100, size=(10, 10))
print(array_10x10)

# array_5x20 = array_10x10.reshape((5, 20))
# print(array_5x20)

# array_20x5 = array_10x10.reshape((20,5))
# print(array_20x5)

# array_1x100 = array_10x10.reshape((1,100))
# print(array_1x100)

# array_100x1 = array_10x10.reshape((100,1))
# print(array_100x1)

# array_2x50 = array_10x10.reshape((2,50))
# print(array_2x50)

# array_50x2 = array_10x10.reshape((50,2))
# print(array_50x2)

# array_4x25 = array_10x10.reshape((4,25))
# print(array_4x25)

# array_25x4 = array_10x10.reshape((25,4))
# print(array_1x100)

shapes = [(5, 20), (20, 5), (2, 50), (50,2), (4, 25), (1, 100), (100,1), (25, 4)]

for shape in shapes:
    reshaped_array = array_10x10.reshape(shape)
    print(reshaped_array)


