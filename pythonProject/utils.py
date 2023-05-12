import math
import time
from math import sqrt

prev_value = time.perf_counter()


def get_simulation_time():
    """Вычисление времени симуляции"""
    global prev_value
    now_value = time.perf_counter()
    delta = now_value - prev_value
    prev_value = now_value
    return delta


def vector_length(coordinates):
    """Длина вектора"""
    value = 0
    for coord in coordinates:
        value += coord ** 2
    return sqrt(value)


def fold_vectors(vector1, vector2):
    """Сложение векторов"""
    return [coord1 + coord2 for coord1, coord2 in zip(vector1, vector2)]


def normalized_vector(vector):
    """Нормализованный вектор"""
    vector_len = vector_length(vector)
    new_vector = []
    for coord in vector:
        new_vector.append(coord / vector_len)
    return tuple(new_vector)


def dot(vector_1, vector_2):
    """Скалярное произведение 2 векторов"""
    value = 0
    for coord_1, coord_2 in zip(vector_1, vector_2):
        value += coord_1 * coord_2
    return value


def normalize_value(value, min_value=float('-INF'), max_value=float('INF')):
    """Нормализация значения"""
    if value < min_value:
        return min_value
    if value > max_value:
        return max_value
    return value


def distance(point1, point2):
    """Расстояние между двумя точками"""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
