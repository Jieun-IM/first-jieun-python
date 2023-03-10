import numpy as np
a = np.arange(0, 32).reshape(4, 4, 2)
a_one = a.flatten()
print(a_one[9])
print(a_one[19])