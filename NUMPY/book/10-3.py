import numpy as np
# 1
np.random.seed(100)
a = np.random.rand(3, 3, 3)
print(a)
# 2
print('a의 원소들 중 최댓값 :',np.max(a))
print('a의 원소들 주 최댓값의 위치 :', np.argmax(a))