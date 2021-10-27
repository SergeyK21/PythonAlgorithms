"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

my_list = [random.randint(-10, 10) for _ in range(20)]
list_below = []
list_pos = []
for i, el in enumerate(my_list):
    if el <0:
        list_below.append(el)
        list_pos.append(i)
print(my_list)
pos = 0
maximum = list_below[pos]
for i, el in enumerate(list_below):
    if maximum < el:
        maximum = el
        pos = list_pos[i]
print(f'Максимольный отрицательный элемент = item[{pos}] = {maximum}')
