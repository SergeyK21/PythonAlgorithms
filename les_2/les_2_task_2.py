"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
num = input('Введите число: ')
if num.isdigit():
    a = 0
    b = 0
    for el in num:
        if int(el) % 2:
            b += 1
        else:
            a += 1
    print(f'Четных цифр - {a}')
    print(f'Нечетных цифр - {b}')
else:
    print('Это не число')
