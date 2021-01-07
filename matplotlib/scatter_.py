from matplotlib import pyplot as plt
import numpy as np


x = np.arange(10)
y = x * 2 + 5

plt.title("Linear curve")
plt.xlabel("x")
plt.ylabel("y = x * 2 + 5")

plt.plot(x, y, 'or')
plt.show()