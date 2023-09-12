import math

import matplotlib.pyplot as plt

t_max = 50
t = [i for i in range(1, t_max)]

def pdf():
    pdf_ = [0.02 * now_t * math.exp(-0.01 * now_t**2) for now_t in t]
    plt.title('Плотность распределения')
    plt.plot(t, pdf_)
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.show()

def draw_time_working():
    R_t = [math.exp(-0.01 * now_t**2) for now_t in t]
    plt.title('Вероятность безотказность работы')
    plt.plot(t, R_t)
    plt.xlabel('t')
    plt.ylabel('R(t)')
    plt.show()


draw_time_working()
pdf()