import numpy as np


a = np.arange(12).reshape(3,4)
print(a)

print(a.mean())
print(a.sum())
print(np.median(a))
print(np.average(a))

print(np.cumsum(a)) #累乘
print(np.diff(a)) #累差

print(np.max(a))
print(np.min(a))

print(np.argmax(a))
print(np.argmin(a))