import numpy as np


a = np.random.randn(3,4)
print(a)

print(a.reshape(2,6))

for i in a.flat:
    print(i, end=" ")

print("\n")

for i in a.flatten(order="F"):
    print(i, end=" ")

print("\n")

for i in a.flatten(order="C"):
    print(i, end=" ")

print("\n")

print(a.ravel(order="F"))

print(a.ravel(order="C"))

#转置
print(a.T)
print(a.transpose())

#插入新维度
print(a[np.newaxis, :])