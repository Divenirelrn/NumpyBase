import numpy as np


a = np.arange(12).reshape(3,4)
print(a)

a.tofile("a.weights")

weight = np.fromfile("a.weights", dtype=np.int)
print(weight)