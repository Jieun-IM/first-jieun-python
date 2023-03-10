import numpy as np

def pprint(arr) :
    print("type:{}".format(type(arr)))
    print("shape: {}, dimension: {}, dtype:{}".format(arr.shape, arr.ndim, arr.dtype))
    print("Array's Data:\n", arr)

a1 = np.arange(1,25).reshape(4,6)    
pprint(a1)

even_arr = a1 % 2 == 0
pprint(even_arr)

print(a1[ even_arr ])
print(np.sum(a1))