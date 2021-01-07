from matplotlib import pyplot as plt

x1 = [2, 5, 8]
y1 = [5, 8, 11]
x2 = [3, 6, 9]
y2 = [6, 10, 10]

plt.title("Bar")
plt.xlabel("x")
plt.ylabel("y")

plt.bar(x1, y1, align="center")
plt.bar(x2, y2, align="center", color="g")

plt.show()