"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
import random


def merge_list(arr, st, mid, end):
    """
    Функция принимает список и 3 параметра,
    полагает, что список отсортирован от start до mid-1 и о
    т mid до end-1, смешивает их и образует новый сортированный список от start до end-1.
    :param arr: массив
    :param st: старт
    :param mid: середина
    :param end: конец
    :return: None
    """
    left = arr[st:mid]
    right = arr[mid:end]
    k = st
    i = j = 0
    while st + i < mid and mid + j < end:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if st + i < mid:
        while k < end:
            arr[k] = left[i]
            i += 1
            k += 1
    else:
        while k < end:
            arr[k] = right[j]
            j += 1
            k += 1


def merge_sort(arr, st, end):
    """
    Функция принимает на вход список и 2 переменные: start и end.
    merge_sort будет сортировать список от start до end-1 индексов.
    :param arr: массив
    :param st: старт
    :param end: конец
    :return: None
    """
    if end - st > 1:
        mid = (st + end) // 2
        merge_sort(arr, st, mid)
        merge_sort(arr, mid, end)
        merge_list(arr, st, mid, end)


arr = [random.random() * 50 for _ in range(10)]
print(arr)

merge_sort(arr, 0, len(arr))
print(arr)
