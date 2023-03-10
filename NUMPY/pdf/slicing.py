import numpy as np

np_array = np.arange(1,17).reshape(4,4)

print(np_array)

print(np_array[0:2])

print(np_array[0:2][0])
print(np_array[0:2, 0])

print(np_array[0:2][1])
print(np_array[0:2, 1])

print(np_array[::2][::2])
print(np_array[::2, ::2])

