import numpy as np

scores = np.array([88,72,93,94,89,78,99])

print(scores[1:4])
print(scores[:-3:-1])

np_array = np.arange(1,10).reshape(3,3)
print(np_array > 5)
print(np_array[ np_array > 5])

print(np_array[:] % 2 == 0)
print(np_array[ np_array % 2 == 0])