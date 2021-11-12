"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;

b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;

c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

d. написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
а проявили творчество, фантазию и создали универсальный код для замера памяти.
"""

import sys
import functools

memory = 0


def show_size(x, name, level=0):
    """
    Проверяет кол-во занимаемой памяти объекта x.
    И распечатывает результат.
    :param x: Объект проверки
    :param name: Наименование
    :param level: Переменная контроля подтиповых объектов
    :return: sys.getsizeof(x)
    """
    print('\t' * level, f'name = {name}, type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}, id = {id(x)}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, ' - ', level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, ' - ', level + 1)
    return sys.getsizeof(x)


def test_memory_func(func, n=None, init_list=None, check_list=None):
    """
    Декоратор с параметрами
    :param init_list: Входные параметры
    :param check_list: Действительный результат
    :return: decorator
    """
    global memory
    memory = 0
    if init_list and check_list:
        for i, el in enumerate(init_list):
            assert check_list[i] == test_memory_func(func, el)
            print(f'Test{i + 1} ОК')
    else:
        return func(n)


def func1(n):
    """
    Исходя из условия задачи, логически можно представить что это геометрическая прогрессия где,
    Переменная q - это знаменатель геометрической прогрессии;
    Переменная a - это это 1-й элемент геометрической прогресии.
    :param n: Колличество членов геометрической прогрессии
    :return: Сумма n первых членов геометрической прогрессии
    """
    global memory
    memory += show_size(n, 'n')
    if n == 0:
        return 'Введите n'
    q = -0.5
    memory += show_size(q, 'q')
    memory += show_size(1 * (q ** n - 1) / (q - 1), 'return')
    return 1 * (q ** n - 1) / (q - 1)


def func2(n):
    """
    Рекурсия
    :param n: Колличество элементов
    :return: Сумма элементов
    """
    global memory
    memory += show_size(n, 'n')
    if n < 1:
        return 0
    q = -0.5
    memory += show_size(q, 'q')
    memory += show_size(1 * (q ** n - 1) / (q - 1), 'return')
    return q ** (n - 1) + func2(n - 1)


def func3(n):
    """
    Цикл
    :param n: Колличество эллементов
    :return: Сумма элементов
    """
    global memory
    item = 1
    memory += show_size(item, 'item')
    summa = 0
    memory += show_size(summa, 'summa')
    memory += show_size(range(n), 'range(n)')
    for i in range(n):
        summa += item
        item /= -2
    return summa


test_memory_func(func1, None, [1, 2, 3, 4, 5, 10, 52],
                 [1.0, 0.5, 0.75, 0.625, 0.6875, 0.666015625, 0.6666666666666665])
memory_f1 = memory
print(f'Общий объем памяти 1й функции: {memory_f1}')
# name = n, type = <class 'int'>, size = 28, object = 1, id = 1281245866288
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 1281255360144
#  name = return, type = <class 'float'>, size = 24, object = 1.0, id = 1281255361840
# Test1 ОК
#  name = n, type = <class 'int'>, size = 28, object = 2, id = 1281245866320
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 1281255360144
#  name = return, type = <class 'float'>, size = 24, object = 0.5, id = 1281255361840
# Test2 ОК
#  name = n, type = <class 'int'>, size = 28, object = 3, id = 1281245866352
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 1281255360144
#  name = return, type = <class 'float'>, size = 24, object = 0.75, id = 1281255361840
# Test3 ОК
#  name = n, type = <class 'int'>, size = 28, object = 4, id = 1281245866384
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 1281255360144
#  name = return, type = <class 'float'>, size = 24, object = 0.625, id = 1281255361840
# Test4 ОК
#  name = n, type = <class 'int'>, size = 28, object = 5, id = 1281245866416
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 1281255360144
#  name = return, type = <class 'float'>, size = 24, object = 0.6875, id = 1281255361840
# Test5 ОК
#  name = n, type = <class 'int'>, size = 28, object = 10, id = 1281245866576
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 1281255360144
#  name = return, type = <class 'float'>, size = 24, object = 0.666015625, id = 1281255361840
# Test6 ОК
#  name = n, type = <class 'int'>, size = 28, object = 52, id = 1281245867920
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 1281255360144
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666666665, id = 1281255361840
# Test7 ОК
# Общий объем памяти 1й функции: 76


test_memory_func(func2, None, [1, 2, 3, 4, 5, 10, 52],
                 [1.0, 0.5, 0.75, 0.625, 0.6875, 0.666015625, 0.6666666666666665])
memory_f2 = memory
print(f'Общий объем памяти 2й функции: {memory_f2}')
# name = n, type = <class 'int'>, size = 28, object = 1, id = 2022115338544
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 1.0, id = 2022121229616
#  name = n, type = <class 'int'>, size = 24, object = 0, id = 2022115338512
# Test1 ОК
#  name = n, type = <class 'int'>, size = 28, object = 2, id = 2022115338576
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.5, id = 2022121228464
#  name = n, type = <class 'int'>, size = 28, object = 1, id = 2022115338544
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 1.0, id = 2022121229584
#  name = n, type = <class 'int'>, size = 24, object = 0, id = 2022115338512
# Test2 ОК
#  name = n, type = <class 'int'>, size = 28, object = 3, id = 2022115338608
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.75, id = 2022121228464
#  name = n, type = <class 'int'>, size = 28, object = 2, id = 2022115338576
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.5, id = 2022121229616
#  name = n, type = <class 'int'>, size = 28, object = 1, id = 2022115338544
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 1.0, id = 2022121229552
#  name = n, type = <class 'int'>, size = 24, object = 0, id = 2022115338512
# Test3 ОК
#  name = n, type = <class 'int'>, size = 28, object = 4, id = 2022115338640
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.625, id = 2022121228464
#  name = n, type = <class 'int'>, size = 28, object = 3, id = 2022115338608
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.75, id = 2022121229616
#  name = n, type = <class 'int'>, size = 28, object = 2, id = 2022115338576
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.5, id = 2022121229584
#  name = n, type = <class 'int'>, size = 28, object = 1, id = 2022115338544
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 1.0, id = 2022121229488
#  name = n, type = <class 'int'>, size = 24, object = 0, id = 2022115338512
# Test4 ОК
#  name = n, type = <class 'int'>, size = 28, object = 5, id = 2022115338672
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6875, id = 2022121228464
#  name = n, type = <class 'int'>, size = 28, object = 4, id = 2022115338640
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.625, id = 2022121229616
#  name = n, type = <class 'int'>, size = 28, object = 3, id = 2022115338608
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.75, id = 2022121229584
#  name = n, type = <class 'int'>, size = 28, object = 2, id = 2022115338576
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.5, id = 2022121229552
#  name = n, type = <class 'int'>, size = 28, object = 1, id = 2022115338544
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 1.0, id = 2022121229520
#  name = n, type = <class 'int'>, size = 24, object = 0, id = 2022115338512
# Test5 ОК
#  name = n, type = <class 'int'>, size = 28, object = 10, id = 2022115338832
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.666015625, id = 2022121228464
#  name = n, type = <class 'int'>, size = 28, object = 9, id = 2022115338800
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.66796875, id = 2022121229616
#  name = n, type = <class 'int'>, size = 28, object = 8, id = 2022115338768
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6640625, id = 2022121229584
#  name = n, type = <class 'int'>, size = 28, object = 7, id = 2022115338736
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.671875, id = 2022121229552
#  name = n, type = <class 'int'>, size = 28, object = 6, id = 2022115338704
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.65625, id = 2022121229488
#  name = n, type = <class 'int'>, size = 28, object = 5, id = 2022115338672
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6875, id = 2022121229424
#  name = n, type = <class 'int'>, size = 28, object = 4, id = 2022115338640
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.625, id = 2022121229456
#  name = n, type = <class 'int'>, size = 28, object = 3, id = 2022115338608
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.75, id = 2022121228432
#  name = n, type = <class 'int'>, size = 28, object = 2, id = 2022115338576
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.5, id = 2022121228400
#  name = n, type = <class 'int'>, size = 28, object = 1, id = 2022115338544
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 1.0, id = 2022121228368
#  name = n, type = <class 'int'>, size = 24, object = 0, id = 2022115338512
# Test6 ОК
#  name = n, type = <class 'int'>, size = 28, object = 52, id = 2022115340176
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666666665, id = 2022121228464
#  name = n, type = <class 'int'>, size = 28, object = 51, id = 2022115340144
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.666666666666667, id = 2022121229616
#  name = n, type = <class 'int'>, size = 28, object = 50, id = 2022115340112
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666666661, id = 2022121229584
#  name = n, type = <class 'int'>, size = 28, object = 49, id = 2022115340080
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666666679, id = 2022121229552
#  name = n, type = <class 'int'>, size = 28, object = 48, id = 2022115340048
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666666643, id = 2022121229488
#  name = n, type = <class 'int'>, size = 28, object = 47, id = 2022115340016
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666666714, id = 2022121229424
#  name = n, type = <class 'int'>, size = 28, object = 46, id = 2022115339984
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666666572, id = 2022121229456
#  name = n, type = <class 'int'>, size = 28, object = 45, id = 2022115339952
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666666856, id = 2022121228432
#  name = n, type = <class 'int'>, size = 28, object = 44, id = 2022115339920
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666666288, id = 2022121228400
#  name = n, type = <class 'int'>, size = 28, object = 43, id = 2022115339888
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666667425, id = 2022121229520
#  name = n, type = <class 'int'>, size = 28, object = 42, id = 2022115339856
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666665151, id = 2022121229392
#  name = n, type = <class 'int'>, size = 28, object = 41, id = 2022115339824
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666669698, id = 2022121229360
#  name = n, type = <class 'int'>, size = 28, object = 40, id = 2022115339792
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666660603, id = 2022121229328
#  name = n, type = <class 'int'>, size = 28, object = 39, id = 2022115339760
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666678793, id = 2022121229296
#  name = n, type = <class 'int'>, size = 28, object = 38, id = 2022115339728
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666642413, id = 2022121229264
#  name = n, type = <class 'int'>, size = 28, object = 37, id = 2022115339696
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666715173, id = 2022121228336
#  name = n, type = <class 'int'>, size = 28, object = 36, id = 2022115339664
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666569654, id = 2022121228304
#  name = n, type = <class 'int'>, size = 28, object = 35, id = 2022115339632
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666860692, id = 2022121228272
#  name = n, type = <class 'int'>, size = 28, object = 34, id = 2022115339600
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666666278616, id = 2022121229232
#  name = n, type = <class 'int'>, size = 28, object = 33, id = 2022115339568
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666667442769, id = 2022121229200
#  name = n, type = <class 'int'>, size = 28, object = 32, id = 2022115339536
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666665114462, id = 2022121229168
#  name = n, type = <class 'int'>, size = 28, object = 31, id = 2022115339504
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666669771075, id = 2022121229136
#  name = n, type = <class 'int'>, size = 28, object = 30, id = 2022115339472
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.666666666045785, id = 2022121228240
#  name = n, type = <class 'int'>, size = 28, object = 29, id = 2022115339440
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666679084301, id = 2022121228208
#  name = n, type = <class 'int'>, size = 28, object = 28, id = 2022115339408
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666641831398, id = 2022121228176
#  name = n, type = <class 'int'>, size = 28, object = 27, id = 2022115339376
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666716337204, id = 2022121229104
#  name = n, type = <class 'int'>, size = 28, object = 26, id = 2022115339344
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666567325592, id = 2022121229072
#  name = n, type = <class 'int'>, size = 28, object = 25, id = 2022115339312
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666865348816, id = 2022121229040
#  name = n, type = <class 'int'>, size = 28, object = 24, id = 2022115339280
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666666269302368, id = 2022121229008
#  name = n, type = <class 'int'>, size = 28, object = 23, id = 2022115339248
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666667461395264, id = 2022121228976
#  name = n, type = <class 'int'>, size = 28, object = 22, id = 2022115339216
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666665077209473, id = 2022121228944
#  name = n, type = <class 'int'>, size = 28, object = 21, id = 2022115339184
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666669845581055, id = 2022121228912
#  name = n, type = <class 'int'>, size = 28, object = 20, id = 2022115339152
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666660308837891, id = 2022121228880
#  name = n, type = <class 'int'>, size = 28, object = 19, id = 2022115339120
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666679382324219, id = 2022121228848
#  name = n, type = <class 'int'>, size = 28, object = 18, id = 2022115339088
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666641235351562, id = 2022121228816
#  name = n, type = <class 'int'>, size = 28, object = 17, id = 2022115339056
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666717529296875, id = 2022121228144
#  name = n, type = <class 'int'>, size = 28, object = 16, id = 2022115339024
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.666656494140625, id = 2022121228112
#  name = n, type = <class 'int'>, size = 28, object = 15, id = 2022115338992
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.66668701171875, id = 2022121228784
#  name = n, type = <class 'int'>, size = 28, object = 14, id = 2022115338960
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6666259765625, id = 2022121228752
#  name = n, type = <class 'int'>, size = 28, object = 13, id = 2022115338928
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.666748046875, id = 2022121228720
#  name = n, type = <class 'int'>, size = 28, object = 12, id = 2022115338896
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.66650390625, id = 2022121228688
#  name = n, type = <class 'int'>, size = 28, object = 11, id = 2022115338864
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6669921875, id = 2022121228656
#  name = n, type = <class 'int'>, size = 28, object = 10, id = 2022115338832
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.666015625, id = 2022121228624
#  name = n, type = <class 'int'>, size = 28, object = 9, id = 2022115338800
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.66796875, id = 2022121228592
#  name = n, type = <class 'int'>, size = 28, object = 8, id = 2022115338768
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6640625, id = 2022121228560
#  name = n, type = <class 'int'>, size = 28, object = 7, id = 2022115338736
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.671875, id = 2022121228528
#  name = n, type = <class 'int'>, size = 28, object = 6, id = 2022115338704
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.65625, id = 2022121228496
#  name = n, type = <class 'int'>, size = 28, object = 5, id = 2022115338672
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.6875, id = 2022121228016
#  name = n, type = <class 'int'>, size = 28, object = 4, id = 2022115338640
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.625, id = 2022121228048
#  name = n, type = <class 'int'>, size = 28, object = 3, id = 2022115338608
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.75, id = 2022121229936
#  name = n, type = <class 'int'>, size = 28, object = 2, id = 2022115338576
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 0.5, id = 2022121229904
#  name = n, type = <class 'int'>, size = 28, object = 1, id = 2022115338544
#  name = q, type = <class 'float'>, size = 24, object = -0.5, id = 2022121227920
#  name = return, type = <class 'float'>, size = 24, object = 1.0, id = 2022121229872
#  name = n, type = <class 'int'>, size = 24, object = 0, id = 2022115338512
# Test7 ОК
# Общий объем памяти 2й функции: 3976


test_memory_func(func3, None, [1, 2, 3, 4, 5, 10, 52],
                 [1.0, 0.5, 0.75, 0.625, 0.6875, 0.666015625, 0.6666666666666665])
memory_f3 = memory
print(f'Общий объем памяти 3й функции: {memory_f3}')
#
#  name = item, type = <class 'int'>, size = 28, object = 1, id = 2308238764336
#  name = summa, type = <class 'int'>, size = 24, object = 0, id = 2308238764304
#  name = range(n), type = <class 'range'>, size = 48, object = range(0, 1), id = 2308244812448
# 	 name =  - , type = <class 'int'>, size = 24, object = 0, id = 2308238764304
# Test1 ОК
#  name = item, type = <class 'int'>, size = 28, object = 1, id = 2308238764336
#  name = summa, type = <class 'int'>, size = 24, object = 0, id = 2308238764304
#  name = range(n), type = <class 'range'>, size = 48, object = range(0, 2), id = 2308244812448
# 	 name =  - , type = <class 'int'>, size = 24, object = 0, id = 2308238764304
# 	 name =  - , type = <class 'int'>, size = 28, object = 1, id = 2308238764336
# Test2 ОК
#  name = item, type = <class 'int'>, size = 28, object = 1, id = 2308238764336
#  name = summa, type = <class 'int'>, size = 24, object = 0, id = 2308238764304
#  name = range(n), type = <class 'range'>, size = 48, object = range(0, 3), id = 2308244812448
# 	 name =  - , type = <class 'int'>, size = 24, object = 0, id = 2308238764304
# 	 name =  - , type = <class 'int'>, size = 28, object = 1, id = 2308238764336
# 	 name =  - , type = <class 'int'>, size = 28, object = 2, id = 2308238764368
# Test3 ОК
#  name = item, type = <class 'int'>, size = 28, object = 1, id = 2308238764336
#  name = summa, type = <class 'int'>, size = 24, object = 0, id = 2308238764304
#  name = range(n), type = <class 'range'>, size = 48, object = range(0, 4), id = 2308244812448
# 	 name =  - , type = <class 'int'>, size = 24, object = 0, id = 2308238764304
# 	 name =  - , type = <class 'int'>, size = 28, object = 1, id = 2308238764336
# 	 name =  - , type = <class 'int'>, size = 28, object = 2, id = 2308238764368
# 	 name =  - , type = <class 'int'>, size = 28, object = 3, id = 2308238764400
# Test4 ОК
#  name = item, type = <class 'int'>, size = 28, object = 1, id = 2308238764336
#  name = summa, type = <class 'int'>, size = 24, object = 0, id = 2308238764304
#  name = range(n), type = <class 'range'>, size = 48, object = range(0, 5), id = 2308244812448
# 	 name =  - , type = <class 'int'>, size = 24, object = 0, id = 2308238764304
# 	 name =  - , type = <class 'int'>, size = 28, object = 1, id = 2308238764336
# 	 name =  - , type = <class 'int'>, size = 28, object = 2, id = 2308238764368
# 	 name =  - , type = <class 'int'>, size = 28, object = 3, id = 2308238764400
# 	 name =  - , type = <class 'int'>, size = 28, object = 4, id = 2308238764432
# Test5 ОК
#  name = item, type = <class 'int'>, size = 28, object = 1, id = 2308238764336
#  name = summa, type = <class 'int'>, size = 24, object = 0, id = 2308238764304
#  name = range(n), type = <class 'range'>, size = 48, object = range(0, 10), id = 2308244812448
# 	 name =  - , type = <class 'int'>, size = 24, object = 0, id = 2308238764304
# 	 name =  - , type = <class 'int'>, size = 28, object = 1, id = 2308238764336
# 	 name =  - , type = <class 'int'>, size = 28, object = 2, id = 2308238764368
# 	 name =  - , type = <class 'int'>, size = 28, object = 3, id = 2308238764400
# 	 name =  - , type = <class 'int'>, size = 28, object = 4, id = 2308238764432
# 	 name =  - , type = <class 'int'>, size = 28, object = 5, id = 2308238764464
# 	 name =  - , type = <class 'int'>, size = 28, object = 6, id = 2308238764496
# 	 name =  - , type = <class 'int'>, size = 28, object = 7, id = 2308238764528
# 	 name =  - , type = <class 'int'>, size = 28, object = 8, id = 2308238764560
# 	 name =  - , type = <class 'int'>, size = 28, object = 9, id = 2308238764592
# Test6 ОК
#  name = item, type = <class 'int'>, size = 28, object = 1, id = 2308238764336
#  name = summa, type = <class 'int'>, size = 24, object = 0, id = 2308238764304
#  name = range(n), type = <class 'range'>, size = 48, object = range(0, 52), id = 2308244812448
# 	 name =  - , type = <class 'int'>, size = 24, object = 0, id = 2308238764304
# 	 name =  - , type = <class 'int'>, size = 28, object = 1, id = 2308238764336
# 	 name =  - , type = <class 'int'>, size = 28, object = 2, id = 2308238764368
# 	 name =  - , type = <class 'int'>, size = 28, object = 3, id = 2308238764400
# 	 name =  - , type = <class 'int'>, size = 28, object = 4, id = 2308238764432
# 	 name =  - , type = <class 'int'>, size = 28, object = 5, id = 2308238764464
# 	 name =  - , type = <class 'int'>, size = 28, object = 6, id = 2308238764496
# 	 name =  - , type = <class 'int'>, size = 28, object = 7, id = 2308238764528
# 	 name =  - , type = <class 'int'>, size = 28, object = 8, id = 2308238764560
# 	 name =  - , type = <class 'int'>, size = 28, object = 9, id = 2308238764592
# 	 name =  - , type = <class 'int'>, size = 28, object = 10, id = 2308238764624
# 	 name =  - , type = <class 'int'>, size = 28, object = 11, id = 2308238764656
# 	 name =  - , type = <class 'int'>, size = 28, object = 12, id = 2308238764688
# 	 name =  - , type = <class 'int'>, size = 28, object = 13, id = 2308238764720
# 	 name =  - , type = <class 'int'>, size = 28, object = 14, id = 2308238764752
# 	 name =  - , type = <class 'int'>, size = 28, object = 15, id = 2308238764784
# 	 name =  - , type = <class 'int'>, size = 28, object = 16, id = 2308238764816
# 	 name =  - , type = <class 'int'>, size = 28, object = 17, id = 2308238764848
# 	 name =  - , type = <class 'int'>, size = 28, object = 18, id = 2308238764880
# 	 name =  - , type = <class 'int'>, size = 28, object = 19, id = 2308238764912
# 	 name =  - , type = <class 'int'>, size = 28, object = 20, id = 2308238764944
# 	 name =  - , type = <class 'int'>, size = 28, object = 21, id = 2308238764976
# 	 name =  - , type = <class 'int'>, size = 28, object = 22, id = 2308238765008
# 	 name =  - , type = <class 'int'>, size = 28, object = 23, id = 2308238765040
# 	 name =  - , type = <class 'int'>, size = 28, object = 24, id = 2308238765072
# 	 name =  - , type = <class 'int'>, size = 28, object = 25, id = 2308238765104
# 	 name =  - , type = <class 'int'>, size = 28, object = 26, id = 2308238765136
# 	 name =  - , type = <class 'int'>, size = 28, object = 27, id = 2308238765168
# 	 name =  - , type = <class 'int'>, size = 28, object = 28, id = 2308238765200
# 	 name =  - , type = <class 'int'>, size = 28, object = 29, id = 2308238765232
# 	 name =  - , type = <class 'int'>, size = 28, object = 30, id = 2308238765264
# 	 name =  - , type = <class 'int'>, size = 28, object = 31, id = 2308238765296
# 	 name =  - , type = <class 'int'>, size = 28, object = 32, id = 2308238765328
# 	 name =  - , type = <class 'int'>, size = 28, object = 33, id = 2308238765360
# 	 name =  - , type = <class 'int'>, size = 28, object = 34, id = 2308238765392
# 	 name =  - , type = <class 'int'>, size = 28, object = 35, id = 2308238765424
# 	 name =  - , type = <class 'int'>, size = 28, object = 36, id = 2308238765456
# 	 name =  - , type = <class 'int'>, size = 28, object = 37, id = 2308238765488
# 	 name =  - , type = <class 'int'>, size = 28, object = 38, id = 2308238765520
# 	 name =  - , type = <class 'int'>, size = 28, object = 39, id = 2308238765552
# 	 name =  - , type = <class 'int'>, size = 28, object = 40, id = 2308238765584
# 	 name =  - , type = <class 'int'>, size = 28, object = 41, id = 2308238765616
# 	 name =  - , type = <class 'int'>, size = 28, object = 42, id = 2308238765648
# 	 name =  - , type = <class 'int'>, size = 28, object = 43, id = 2308238765680
# 	 name =  - , type = <class 'int'>, size = 28, object = 44, id = 2308238765712
# 	 name =  - , type = <class 'int'>, size = 28, object = 45, id = 2308238765744
# 	 name =  - , type = <class 'int'>, size = 28, object = 46, id = 2308238765776
# 	 name =  - , type = <class 'int'>, size = 28, object = 47, id = 2308238765808
# 	 name =  - , type = <class 'int'>, size = 28, object = 48, id = 2308238765840
# 	 name =  - , type = <class 'int'>, size = 28, object = 49, id = 2308238765872
# 	 name =  - , type = <class 'int'>, size = 28, object = 50, id = 2308238765904
# 	 name =  - , type = <class 'int'>, size = 28, object = 51, id = 2308238765936
# Test7 ОК
# Общий объем памяти 3й функции: 100


""" 
Быто произведено 7 тестов 4 задачи из 2-го урока:
    "Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
    Количество элементов (n) вводится с клавиатуры."
Входные параметры:
    init_list = [1, 2, 3, 4, 5, 10, 52]
Параметры дествительных результатов: 
    check_list = [1.0, 0.5, 0.75, 0.625, 0.6875, 0.666015625, 0.6666666666666665]
Все функции тестирование прошли успешно. 
Вывод:
    Наиболее эффективное использзование памяти у 1й функции.
"""