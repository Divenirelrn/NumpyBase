import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

print(a[0, 1])
print(a[:,1])
print(a[...])

for col in a.T:
    print(col)

for ele in a.flat:
    print(ele)

for ele in np.nditer(a):
    print(ele)