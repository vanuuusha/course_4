import numpy as np
import matplotlib.pyplot as plt

T = 50
raspr_lambda = 1 / T
t_max = 500
t = np.array([i for i in range(1, t_max)])
R_t = np.exp(-raspr_lambda * t)

plt.plot(t, R_t)
plt.title('Вероятность безотказной работы')
plt.xlabel('t')
plt.ylabel('R(t)')
plt.show()