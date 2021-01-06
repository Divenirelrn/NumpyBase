import numpy as np


a = np.arange(10).reshape([2,5])
print(a)

b = a.copy() #deep copy
print(b)

c = a.copy(order="C") #行序
print(c)
for ele in np.nditer(c):
    print(ele, end=" ")
print("\n")

d = a.copy(order="F") #列序
print(d)
for ele in np.nditer(d):
    print(ele, end=" ")
