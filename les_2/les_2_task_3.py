"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
num = int(input('Введите число: '))
revers_num = ''
while num:
    revers_num += str(num % 10)
    num //= 10
print(revers_num)
