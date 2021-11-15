"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
"""
import random


def get_median(arr):
    """
    Нахождение медианы массива размером 2m + 1, где m — натуральное число, заполнен случайным образом.
    :param arr: Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
    :return: [медиана, [массив вычитаемых минимумов длиной = (len(arr) // 2) + 1]
                    + [остатотк от вычитания из массива arr длиной = len(arr) // 2]]
    """
    right = arr[:]
    left = []
    c = (len(arr) // 2) + 1
    while len(right) >= (len(arr) // 2) + 1:
        minimum = right[0]
        index = 0
        for i in range(len(right)):
            if minimum > right[i]:
                minimum = right[i]
                index = i
        left.append(right.pop(index))
    return [left[len(left) - 1], left + right]


size = random.randint(4, 20)
arr = [random.randint(1, 50) for i in range(2 * size + 1)]
print(arr)
result = get_median(arr)
print(f'Медиана данного массива = {result[0]}')
print(f'Собственно сам массив: {result[1]}')
