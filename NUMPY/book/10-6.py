import numpy as np
x1 = [i for i in range(100)]
x2 = [i + np.random.randint(1, 10) for i in range(100)]
x3 = [i + np.random.randint(1, 50) for i in range(100)]
x4 = [np.random.randint(1, 100) for i in range(100)]
result = np.corrcoef( [x1, x2, x3, x4])
print(result)


# 걍 내가 확인해보고 싶은 거
print(x1)
print(x2)
print(x3)
print(x4)