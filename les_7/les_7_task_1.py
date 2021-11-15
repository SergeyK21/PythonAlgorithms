"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
from random import shuffle

arr_1 = [i for i in range(-100, 100)]
shuffle(arr_1)
arr_2 = arr_1[:]
count_ar = 0


def bubble_sort(arr):
    """
    while заменен на for.
    Переменная count_ar служит для посчета колличества проходов.
    Сортировка пузырьком.
    :param arr: массив
    :return: None
    """
    global count_ar
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        count_ar += 1


def advanced_bubble_sorting(arr):
    """
    while заменен на for.
    Переменная count_ar служит для посчета колличества проходов.
    Усовершенствованная сортировка пузырьком.
    Если условие (if arr[j] > arr[j + 1]) во втором цикле ни разу не выполнилось,
    значит фрагмент массива и сам массив отсортирован.
    Переменная flag служит для вызова return.
    :param arr: массив
    :return: None (Прекращает работу функции при выполнении условя (if flag))
    """
    global count_ar
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            return
        count_ar += 1


print('Неотсортированный массив:')
print(arr_1)
bubble_sort(arr_1)
print(f'Обычная сортировка пузырьком отсортировала за {count_ar} проходов')
print(arr_1)
print()
print('*' * 900)
print()
print('Неотсортированный массив:')
print(arr_2)
count_ar = 0
advanced_bubble_sorting(arr_2)
print(f'Усовершенствованная сортировка пузырьком отсортировала за {count_ar} проходов')
print(arr_2)
