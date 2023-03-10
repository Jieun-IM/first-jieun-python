import numpy as np
arr = np.arange(1,25).reshape((4,6))
print(arr)

# case 1
print([arr[0,0], arr[1,1], arr[2,2], arr[3,3]])
print(arr[[0,1,2,3], [0,1,2,3]])

# case 2
print(arr[:, [1,2]]) 
# 전체 행에 대해, 1,2번 열 참조
