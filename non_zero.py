import numpy as np


a = np.random.rand(3,4)
print(a)

a = a > 0.5
print(a)

print(np.nonzero(a))