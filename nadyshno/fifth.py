import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

t_max = 50
t = np.array([i for i in range(1, t_max)])
T = np.array([12, 31, 28, 22])
lambdas = np.ones_like(T) / T
width = np.array([0.19, 0.21, 0.14, 0.46])


def pdf_():
    all_pdf = []
    for i in lambdas:
        all_pdf.append(i * np.exp(-i*t))
    all_pdf = np.array(all_pdf)
    now_width = np.reshape(width, (-1, 1))
    pdf_ = np.sum(now_width * all_pdf, axis=0)
    plt.title('Плотность распределения')
    plt.plot(t, pdf_)
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.show()


def R_t():
    all_R_t = []
    for i in lambdas:
        all_R_t.append(np.exp(-i*t))
    all_R_t = np.array(all_R_t)
    now_width = np.reshape(width, (-1, 1))
    R_t = np.sum(now_width * all_R_t, axis=0)
    plt.title('Вероятность безотказность работы')
    plt.plot(t, R_t)
    plt.xlabel('t')
    plt.ylabel('R(t)')
    plt.show()


def lambda_t():
    all_R_t = []
    for i in lambdas:
        all_R_t.append(np.exp(-i*t))
    all_R_t = np.array(all_R_t)
    now_width = np.reshape(width, (-1, 1))
    R_t = np.sum(now_width * all_R_t, axis=0)
    all_pdf = []
    for i in lambdas:
        all_pdf.append(i * np.exp(-i * t))
    all_pdf = np.array(all_pdf)
    now_width = np.reshape(width, (-1, 1))
    pdf_ = np.sum(now_width * all_pdf, axis=0)

    plt.title('Интенивность отказов')
    plt.plot(t, pdf_ / R_t)
    plt.xlabel('t')
    plt.ylabel('lambda(t)')
    plt.show()


pdf_()
R_t()
lambda_t()