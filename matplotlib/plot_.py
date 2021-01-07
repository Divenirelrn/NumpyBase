import matplotlib
from matplotlib import pyplot as plt
import numpy as np


zh_font = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")

x = np.arange(12)
y = x * 2 + 5

plt.title("线性函数", fontproperties=zh_font)
plt.xlabel("x")
plt.ylabel("y = x * 2 + 5")

plt.plot(x, y)
plt.show()
