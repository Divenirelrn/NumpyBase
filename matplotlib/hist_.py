from matplotlib import pyplot as plt
import numpy as np


x = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
hist, bins = np.histogram(x, bins = [0, 20, 40, 60, 80, 100])
print(hist, bins)

plt.title("histogram")

plt.hist(x, bins=[0, 20, 40, 60, 80, 100], rwidth=0.8)
plt.show()