"""
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random

a = []
b = []
c = []
print('Введите диапазон целых чисел')
a.append(int(input('Введите нижнюю грацицу: ')))
a.append(int(input('Введите верхнюю грацицу: ')))
if a[0] < a[1]:
    print('Введите диапазон для вещественных чисел')
    b.append(float(input('Введите нижнюю грацицу: ')))
    b.append(float(input('Введите верхнюю грацицу: ')))
    if b[0] < b[1]:
        print('Введите диапазон для символов, учитывая алфавитный порядок')
        c.append(input('Введите нижнюю грацицу: ')[0])
        c.append(input('Введите верхнюю грацицу: ')[0])
        if c[0] < c[1]:
            new_a = random.randint(a[0], a[1])
            new_b = random.uniform(b[0], b[1])
            new_c = chr(random.randint(ord(c[0]), ord(c[1])))
            print(new_a)
            print(new_b)
            print(new_c)
        else:
            print("Некорректно введен диапазон")
    else:
        print("Некорректно введен диапазон")
else:
    print("Некорректно введен диапазон")
