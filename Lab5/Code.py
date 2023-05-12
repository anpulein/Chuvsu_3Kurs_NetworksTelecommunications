import math
import statistics

import matplotlib.pyplot as plt




delay_times = []

# открытие файла и чтение строк
with open('pings.txt', 'r', encoding='utf-16') as file:
    lines = file.readlines()

    # перебор строк и извлечение времени задержки
    for line in lines:
        if "time=" in line:
            time_str = line.split('time=')[1].split()[0]
            time = float(time_str)
            delay_times.append(time)

# построение гистограммы
plt.hist(delay_times, bins=50)

# добавление подписей к осям и заголовка
plt.xlabel('Задержка (мс)')
plt.ylabel('Частота')
plt.title('Диаграмма разброса задержек')

# вывод гистограммы на экран
plt.show()


# Вычисление Джиттера
def calculate_jitter(times):
    mean_delay = statistics.mean(times)
    differences = [delay - mean_delay for delay in times]
    sum_of_squares = sum([diff ** 2 for diff in differences])
    variance = sum_of_squares / (len(times) - 1)
    jitter = math.sqrt(variance)
    return jitter

jitter = calculate_jitter(delay_times)
print("Джиттер = ", jitter)
