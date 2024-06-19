import matplotlib.pyplot as plt
import random
import numpy as np

mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов
data = np.random.normal(mean, std_dev, num_samples)
plt.hist(data, bins=6)
plt.xlabel('x ось')
plt.ylabel('y ось')
plt.title('Создание гистограммы для случайных данных')

plt.show()
