import numpy as np
x = np.array([['a', 'b', 'c', 'd'],
              ['c', 'c', 'g', 'h']])

print(x[ x == 'c'])

mat_a = np.array( [[10, 20, 30], [10, 20, 30]])
mat_b = np.array( [[2, 2, 2], [1, 2, 3]])

print(mat_a - mat_b)