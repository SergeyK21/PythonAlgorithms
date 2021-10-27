"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

"""Первый вариант"""
my_list = [random.randint(0, 10) for _ in range(20)]
print(*my_list)
print(f'Первый вариант - Часто встречающейся элемент {max(set(my_list), key=my_list.count)}')
"""Второй вариант"""
set_1 = set(my_list)
dict_1 = {}
for el in set_1:
    dict_1[el] = 0
for el in my_list:
    dict_1[el] += 1
key_max = []
maximum = dict_1[my_list[0]]
for key, item in dict_1.items():
    if item > maximum:
        maximum = item
for key, value in dict_1.items():
    if maximum == value:
        key_max.append(key)
if (len(key_max) == 1):
    print(f'Второй вариант - Часто встречающейся элемент {key_max[0]}')
else:
    print(f'Второй вариант - Часто встречающиеся элементы {key_max} - встречаются одинаковое кол-во раз')
