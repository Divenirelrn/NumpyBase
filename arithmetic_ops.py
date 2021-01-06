import numpy as np


a = np.arange(12).reshape(3,4)
b = np.array([1,2,3,4])
#+/-/*//
print(a + b)
print(np.add(a,b))
print(a - b)
print(np.subtract(a,b))
print(a * b)
print(np.multiply(a, b))
print(a / b)
print(np.divide(a,b))

#矩阵运算
a = np.array([[1,2],
              [3,4]])
b = np.array([[2,2],
              [2,2]])
print(a.dot(b))
print(np.matmul(a, b))
print(np.vdot(a, b)) #内积和
print(np.inner(a,b)) #内积

#pow, sqrt
print(np.power(a, 2))
print(np.mod(a, 2))

#math function
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))



