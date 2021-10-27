"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

my_list = [random.randint(0, 5) for _ in range(20)]
print(*my_list)
pos_min = 0
pos_max = 0
maximum = my_list[pos_max]
minimum = my_list[pos_min]
summa = 0
for i, el in enumerate(my_list):
    if maximum < el:
        maximum = el
        pos_max = i
    if minimum > el:
        minimum = el
        pos_min = i
if pos_max > pos_min:
    pos_min += 1
    for i in range(pos_min, pos_max):
        summa += my_list[i]
else:
    pos_max += 1
    for i in range(pos_max, pos_min):
        summa += my_list[i]
print(summa)
