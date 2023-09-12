import math

import matplotlib.pyplot as plt

raspr_lambda = 1 / 24
n = 2
t_max = 500
t = [i for i in range(1, t_max)]
def draw_time_working():
    F = [math.exp(-raspr_lambda*now_time)*sum([(raspr_lambda*now_time)**k / math.factorial(k) for k in range(0, n)]) for now_time in t]
    plt.title('Вероятность безотказность работы')
    plt.plot(t, F)
    plt.xlabel('t')
    plt.ylabel('R(t)')
    plt.show()

def draw_intensiv():
    intensiv = [(raspr_lambda ** n * now_t ** (n-1)) / math.factorial(n-1) * 1 / sum([(raspr_lambda*now_t)**k / math.factorial(k) for k in range(0, n)]) for now_t in t]
    plt.title('Интенсивность')
    plt.plot(t, intensiv)
    plt.xlabel('t')
    plt.ylabel('lambda(t)')
    plt.show()


def pdf():
    pdf_ = [(raspr_lambda ** n * now_t ** (n-1)) / math.factorial(n-1) * math.exp(-raspr_lambda*now_t) for now_t in t]
    plt.title('Плотность распределения')
    plt.plot(t, pdf_)
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.show()

draw_time_working()
draw_intensiv()
pdf()