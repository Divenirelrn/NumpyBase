from matplotlib import pyplot as plt
import numpy as np


x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2,1,1)
plt.title("sinx")
plt.plot(x, y1)

plt.subplot(2,1,2)
plt.title("cosx")
plt.plot(x, y2)

plt.show()