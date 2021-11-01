"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:

a. выбрать хорошую задачу, которую имеет смысл оценивать,

b. написать 3 варианта кода (один у вас уже есть),

c. проанализировать 3 варианта и выбрать оптимальный,

d. результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),

e. написать общий вывод: какой из трёх вариантов лучше и почему.

Возьмем для рассмотрения 4 задачу из 2-го урока:
"Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры."
"""
import functools
import cProfile


def decorator_test_func(init_list, check_list):
    """
    Декоратор с параметрами
    :param init_list: Входные параметры
    :param check_list: Действительный результат
    :return: decorator
    """

    def decorator(func):
        def wrapped():
            for i, el in enumerate(init_list):
                assert check_list[i] == func(el)
                print(f'Test{i} ОК')

        return wrapped

    return decorator


def test_func(func):
    """
    Тестировачная функция
    :param func: Тестируемая функция
    :return:
    """
    init_list = [1, 2, 3, 4, 5, 10, 52]
    check_list = [1.0, 0.5, 0.75, 0.625, 0.6875, 0.666015625, 0.6666666666666665]
    for i, el in enumerate(init_list):
        assert check_list[i] == func(el)
        print(f'Test{i} ОК')


# @decorator_test_func([1, 2, 3, 4, 5, 10, 52], [1.0, 0.5, 0.75, 0.625, 0.6875, 0.666015625, 0.6666666666666665])
def func1(n):
    """
    Исходя из условия задачи, логически можно представить что это геометрическая прогрессия где,
    Переменная q - это знаменатель геометрической прогрессии;
    Переменная a - это это 1-й элемент геометрической прогресии.
    :param n: Колличество членов геометрической прогрессии
    :return: Сумма n первых членов геометрической прогрессии
    """
    if n == 0:
        return 'Введите n'
    q = -0.5
    a = 1
    return a * (q ** n - 1) / (q - 1)


"""Тестирование функции с применением декоратора"""
# @decorator_test_func([1, 2, 3, 4, 5, 10, 52], [1.0, 0.5, 0.75, 0.625, 0.6875, 0.666015625, 0.6666666666666665])
# func1()
# Test0 ОК
# Test1 ОК
# Test2 ОК
# Test3 ОК
# Test4 ОК
# Test5 ОК
# Test6 ОК
# "les_4_task_1.func1(1)"
# 1000 loops, best of 5: 335 nsec per loop
# "les_4_task_1.func1(2)"
# 1000 loops, best of 5: 365 nsec per loop
# "les_4_task_1.func1(3)"
# 1000 loops, best of 5: 363 nsec per loop
# "les_4_task_1.func1(4)"
# 1000 loops, best of 5: 382 nsec per loop
# "les_4_task_1.func1(5)"
# 1000 loops, best of 5: 400 nsec per loop
# "les_4_task_1.func1(10)"
# 1000 loops, best of 5: 373 nsec per loop
# "les_4_task_1.func1(52)"
# 1000 loops, best of 5: 382 nsec per loop
# cProfile.run("func1(52)")
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:58(func1)


def func2(n):
    """
    Рекурсия
    :param n: Колличество элементов
    :return: Сумма элементов
    """
    if n < 1:
        return 0
    q = -0.5
    return q ** (n - 1) + func2(n - 1)


"""Тестирование функции:"""
# test_func(func2)
# Test0 ОК
# Test1 ОК
# Test2 ОК
# Test3 ОК
# Test4 ОК
# Test5 ОК
# Test6 ОК
# "les_4_task_1.func2(1)"
# 1000 loops, best of 5: 279 nsec per loop
# "les_4_task_1.func2(2)"
# 1000 loops, best of 5: 481 nsec per loop
# "les_4_task_1.func2(3)"
# 1000 loops, best of 5: 648 nsec per loop
# "les_4_task_1.func2(4)"
# 1000 loops, best of 5: 870 nsec per loop
# "les_4_task_1.func2(5)"
# 1000 loops, best of 5: 1.09 usec per loop
# "les_4_task_1.func2(10)"
# 1000 loops, best of 5: 2.23 usec per loop
# "les_4_task_1.func2(52)"
# 1000 loops, best of 5: 11.9 usec per loop
# cProfile.run("func2(1)")
# 2/1    0.000    0.000    0.000    0.000 les_4_task_1.py:104(func2)
# cProfile.run("func2(2)")
# 3/1    0.000    0.000    0.000    0.000 les_4_task_1.py:104(func2)
# cProfile.run("func2(3)")
# 4/1    0.000    0.000    0.000    0.000 les_4_task_1.py:104(func2)
# cProfile.run("func2(4)")
# 5/1    0.000    0.000    0.000    0.000 les_4_task_1.py:104(func2)
# cProfile.run("func2(5)")
# 6/1    0.000    0.000    0.000    0.000 les_4_task_1.py:104(func2)
# cProfile.run("func2(10)")
# 11/1    0.000    0.000    0.000    0.000 les_4_task_1.py:104(func2)
# cProfile.run("func2(52)")
# 53/1    0.000    0.000    0.000    0.000 les_4_task_1.py:104(func2)


# @decorator_test_func([1, 2, 3, 4, 5, 10, 52], [1.0, 0.5, 0.75, 0.625, 0.6875, 0.666015625, 0.6666666666666665])
def func3(n):
    """
    Цикл
    :param n: Колличество эллементов
    :return: Сумма элементов
    """
    item = 1
    summa = 0
    for i in range(n):
        summa += item
        item /= -2
    return summa


"""Тестирование функции с применением декоратора"""
# @decorator_test_func([1, 2, 3, 4, 5, 10, 52], [1.0, 0.5, 0.75, 0.625, 0.6875, 0.666015625, 0.6666666666666665])
# Test0 ОК
# Test1 ОК
# Test2 ОК
# Test3 ОК
# Test4 ОК
# Test5 ОК
# Test6 ОК
# "les_4_task_1.func3(1)"
# 1000 loops, best of 5: 310 nsec per loop
# "les_4_task_1.func3(2)"
# 1000 loops, best of 5: 393 nsec per loop
# "les_4_task_1.func3(3)"
# 1000 loops, best of 5: 431 nsec per loop
# "les_4_task_1.func3(4)"
# 1000 loops, best of 5: 504 nsec per loop
# "les_4_task_1.func3(5)"
# 1000 loops, best of 5: 565 nsec per loop
# "les_4_task_1.func3(10)"
# 1000 loops, best of 5: 776 nsec per loop
# "les_4_task_1.func3(53)"
# 1000 loops, best of 5: 2.81 usec per loop
# cProfile.run("func3(52)")
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:156(func3)


@functools.lru_cache()
def func4(n):
    """
    Рекурсия + мемоизация
    :param n: Колличество элементов
    :return: Сумма элементов
    """
    if n < 1:
        return 0
    q = -0.5
    return q ** (n - 1) + func2(n - 1)


"""Тестирование функции:"""
# test_func(func4)
# Test0 ОК
# Test1 ОК
# Test2 ОК
# Test3 ОК
# Test4 ОК
# Test5 ОК
# Test6 ОК
# "les_4_task_1.func4(1)"
# 1000 loops, best of 5: 122 nsec per loop
# "les_4_task_1.func4(2)"
# 1000 loops, best of 5: 124 nsec per loop
# "les_4_task_1.func4(3)"
# 1000 loops, best of 5: 129 nsec per loop
# "les_4_task_1.func4(4)"
# 1000 loops, best of 5: 130 nsec per loop
# "les_4_task_1.func4(5)"
# 1000 loops, best of 5: 126 nsec per loop
# "les_4_task_1.func4(10)"
# 1000 loops, best of 5: 127 nsec per loop
# "les_4_task_1.func4(52)"
# 1000 loops, best of 5: 119 nsec per loop
# cProfile.run("func4(1)")
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:196(func4)
# cProfile.run("func4(2)")
# 2/1    0.000    0.000    0.000    0.000 les_4_task_1.py:101(func2)
# cProfile.run("func4(3)")
# 3/1    0.000    0.000    0.000    0.000 les_4_task_1.py:101(func2)
# cProfile.run("func4(4)")
# 4/1    0.000    0.000    0.000    0.000 les_4_task_1.py:101(func2)
# cProfile.run("func4(5)")
# 5/1    0.000    0.000    0.000    0.000 les_4_task_1.py:101(func2)
# cProfile.run("func4(10)")
# 10/1    0.000    0.000    0.000    0.000 les_4_task_1.py:101(func2)
# cProfile.run("func4(52)")
# 52/1    0.000    0.000    0.000    0.000 les_4_task_1.py:101(func2)


"""
Вывод: 
Самый быстрый способ найти сумму ряда использовать функцию func4()
"""