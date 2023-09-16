import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

t_max = 5000
t = [i for i in range(1, t_max)]
T = 200
d = 30



def R_t():
    R_t = np.array([norm.cdf((T-now_t)/d) for now_t in t])
    plt.title('Вероятность безотказность работы')
    plt.plot(t, R_t)
    plt.xlabel('t')
    plt.ylabel('R(t)')
    plt.show()


def pdf():
    y1 = []
    y2 = []
    for num, now_t in enumerate(t):
        cdf = norm.cdf((200 - now_t)/30, 0, 1)
        y1.append(math.exp(-((200-now_t)/30)**2/2) / (30*math.sqrt(2*math.pi) * cdf))
        y2.append((now_t-200) / 900)
    y = []
    for num, _ in enumerate(y1):
        if abs(y1[num] - y2[num]) < 0.006 or y1[num] == 0:
            y.append(y2[num])
        else:
            y.append(y1[num])
    plt.title('Интенивность отказов')
    plt.plot(t, y)
    plt.xlabel('t')
    plt.ylabel('lambda(t)')
    plt.show()

R_t()
pdf()