import matplotlib.pyplot as plt
import random
import numpy as np


x = np.random.rand(5)
y = np.random.rand(5)

plt.scatter(x, y)

plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния для случайных чисел")

plt.show()
