import numpy as np
# 1
n_arr = (np.arange(1, 26) %2).reshape(5, 5)
print(n_arr)
# 2
print('행렬의 행 방향 성분의 합 :')
print(n_arr.sum(axis=0))