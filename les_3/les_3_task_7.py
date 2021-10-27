"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
import random

my_list = [random.randint(0, 100) for _ in range(50)]
print(my_list)
pos_min = 0
minimum1 = my_list[pos_min]
for i, el in enumerate(my_list):
    if el < minimum1:
        minimum1 = el
        pos_min = i
if pos_min != 0 or len(my_list) != 1:
    minimum2 = my_list[0]
else:
    minimum2 = my_list[1]
for i, el in enumerate(my_list):
    if el < minimum2 and i != pos_min:
        minimum2 = el
print(minimum1)
print(minimum2)
