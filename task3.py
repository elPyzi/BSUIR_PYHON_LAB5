import numpy as np
import matplotlib.pyplot as plt


x_values = np.linspace(-5, 12, 100)  # интервал для x
a_values = np.arange(-5, 12.1, 2.5)   # значения параметра a


def f(x, a):
    return x * np.sin(x / 3) + 1.2 * a


function_values = [f(x_values, a) for a in a_values]


for i, a in enumerate(a_values):
    print(f'a = {a}: x = {x_values}, f(x) = {function_values[i]}')


max_value = np.max(function_values)
min_value = np.min(function_values)
average_value = np.mean(function_values)
num_elements = len(function_values)


print(f'Наибольшее значение: {max_value}')
print(f'Наименьшее значение: {min_value}')
print(f'Среднее значение: {average_value}')
print(f'Количество элементов: {num_elements}')


sorted_function_values = [np.sort(arr) if i % 2 == 0 else np.sort(arr)[::-1] for i, arr in enumerate(function_values)]


plt.figure(figsize=(10, 6))


for i, a in enumerate(a_values):
    plt.plot(x_values, function_values[i], label=f'a = {a}', marker='o')

# График прямой, значение которой равно среднему значению функции
plt.axhline(y=average_value, color='r', linestyle='--', label='Среднее значение')

# Оформление графика
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
