"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
print('Введите три разных числа.')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if (a > b and a < c) or (a < b and a > c):
    print(f'Среднее - {a}')
elif (b > a and b < c) or (b < a and b > c):
    print(f'Среднее - {b}')
else:
    print(f'Среднее - {c}')