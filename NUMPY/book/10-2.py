import numpy as np
# 1
n_arr = np.arange(25).reshape(5, 5)
print(n_arr)
# 2
print('첫 원소 :', n_arr[0][0])
print('마지막 원소 :', n_arr[-1][-1])
# 3
print(n_arr[0:2])
# 4
print(n_arr[2:])
# 5
print(n_arr[:, : :2])
# 6
print(n_arr[::2,::2])
# 7
print(n_arr[:2].reshape(5,2))