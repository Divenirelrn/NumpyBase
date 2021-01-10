import numpy as np


arr = np.array([1,2,3], dtype=np.float32)
print(arr)

arr = np.empty([2,3])
print(arr)

arr = np.ones([2,3])
print(arr)

arr = np.zeros(([2,3]))
print(arr)

arr = np.arange(10)
print(arr)

arr = np.asarray([1,2,3])
print(arr)

arr = np.linspace(1, 10, 10)
print(arr)

arr = np.logspace(0, 1, 10)
print(arr)

arr = np.full((3, 4), 128)
print(arr)