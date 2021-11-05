"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк.
Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую
в данной задаче под запретом.
"""
from collections import deque, ChainMap
from functools import reduce

hex_dict = ChainMap({
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}, {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
})


def hex_dec(hex_num):
    """
    Возвращает десятичное число
    :param hex_num: шеснадцатеричное число
    :return: num
    """
    num = 0
    f = len(hex_num) - 1
    for i in hex_num:
        num += hex_dict[i] * 16 ** f
        f -= 1
    return num


def numbers_hex_summa(number_1, number_2):
    """
    Суммирует два шеснадцатеричных числа.
    :param number_1: deque([])
    :param number_2: deque([])
    :return: deque([])
    """
    if len(number_1) >= len(number_2):
        for i in range(len(number_1) - len(number_2)):
            number_2.appendleft('0')
    else:
        for i in range(len(number_2) - len(number_1)):
            number_1.appendleft('0')
    remains = 0
    result = deque()
    for i in range(len(number_1) - 1, -1, -1):
        result.appendleft(hex_dict[(hex_dict[number_1[i]] + hex_dict[number_2[i]] + remains) % 16])
        remains = (hex_dict[number_1[i]] + hex_dict[number_2[i]] + remains) // 16
    while remains != 0:
        result.appendleft(hex_dict[remains % 16])
        remains = remains // 16
    return result


number_1 = deque(input('Введите первое шестнадцатеричное число: ').upper())
number_2 = deque(input('Введите второе шестнадцатеричное число: ').upper())

# number_1 = deque('A2')
# number_2 = deque('C4F')

print(f'Сумма чисел: {numbers_hex_summa(number_1, number_2)}')
list_reduce = [number_2] * hex_dec(number_1)
print(f'Произведение чисел: {reduce(numbers_hex_summa, list_reduce)}')
