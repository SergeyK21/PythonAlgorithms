"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

list_1 = [random.randint(0, 10) for _ in range(5)]
print(*list_1)
maximum = list_1[0]
minimum = list_1[0]
pos_max = 0
pos_min = 0
for i, el in enumerate(list_1):
    if maximum < el:
        maximum = el
        pos_max = i
    if minimum > el:
        minimum = el
        pos_min = i
if pos_max != pos_min:
    list_1[pos_max], list_1[pos_min] = list_1[pos_min], list_1[pos_max]
    print(*list_1)
