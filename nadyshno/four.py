import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

t_max = 500
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
    pdf_ = np.array([norm.pdf((T - now_t) / d) for now_t in t])
    R_t = np.array([norm.cdf((T-now_t)/d) for now_t in t])
    plt.title('Интенивность отказов')
    plt.plot(t, pdf_/R_t)
    plt.xlabel('t')
    plt.ylabel('lambda(t)')
    plt.show()

R_t()
pdf()