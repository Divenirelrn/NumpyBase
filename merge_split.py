import numpy as np


a = np.random.rand(2,3,28,28)
b = np.random.rand(2, 3, 28, 28)
c = np.random.rand(2, 3, 28, 28)

#merge
print(np.vstack((a, b)).shape)
print(np.hstack((a,b)).shape)

print(np.concatenate((a,b,c)).shape)

#split
aa, bb = np.split(a, 2, axis=0)
print(aa.shape, bb.shape)

aa, bb = np.vsplit(a, 2)
print(aa.shape, bb.shape)

aa, bb, cc = np.hsplit(a, 3) #均等分割
print(aa.shape, bb.shape, cc.shape)

aa, bb, cc = np.array_split(a, 3, axis=0) #不均等分割
print(aa.shape, bb.shape, cc.shape)

