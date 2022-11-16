# Дана функция f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

import time
from sympy import symbols, sin, cos
from sympy.plotting import plot
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy


# График функции при помощи библиотеки matplotlib:
def function_graph(min, max):
    x = symbols('x')
    x = [x for x in range(min, max)]
    y = [(-12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30) for
         x in range(min, max)]
    plt.plot(x, y)
    plt.grid()
    plt.show()


# Определить корни
def f_roots(x):
    return -12 * x ** 4 * numpy.sin(
        numpy.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30


def solution():
    global min_value, max_value
    temp = min_value
    max_value = max_value
    roots = []
    interval = []

    while temp < max_value:
        if f_roots(temp) >= 0 and f_roots(temp + 1) <= 0:
            w = fsolve(f_roots, temp)
            roots.append(*w)
        if f_roots(temp) <= 0 and f_roots(temp + 1) >= 0:
            w = fsolve(f_roots, temp)
            roots.append(*w)
        if f_roots(temp) > f_roots(temp + 1) < f_roots(temp + 2):
            interval.append(temp + 1)
        temp += 1
    roots = [round(i, 2) for i in roots]
    print(f'Корни уравнения для заданного интервала: {roots}')
    return roots


# Определить промежутки, на которых f>0 и f<0:
def func_interval(left, right):
    array = []
    temp = left
    while left < right:
        array.append([f_roots(left), left])
        left += 0.1
    if array[0][0] > 0:
        print(f'f > 0 в промежутке {temp, right}')
        return max(array)
    else:
        print(f'f < 0 в промежутке {temp, right}')
        return min(array)


# Вычисляем координаты вершины функции на заданном интервале:
def maximum_and_minimum():
    roots = solution()

    if len(roots) < 2:
        print('На заданном интервале нет вершин')
    else:
        top = []
        for i in range(len(roots) - 1):
            top.append(func_interval(roots[i], roots[i + 1]))
        for j in top:
            j = [round(i, 2) for i in j]
            print(f'Координаты вершин функции: [{j[1]}, {j[0]}]')
        if len(top) < 2:
            print('error')
        else:
            for i in range(len(top) - 1):
                if top[i][0] > top[i + 1][0]:
                    print('Функция убывает')
                else:
                    print('Функция возрастает')


funcrange = list(
    map(int, input('Задайте интервал функции через пробел: ').split()))
min_value = min(funcrange)
max_value = max(funcrange)


# График функции:
function_graph(min_value, max_value)
time.sleep(1)
# Корни функции и интервалы, на которых функция возрастает и убывает
maximum_and_minimum()
