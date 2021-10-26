"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

print('Вводите натуральные числа. Для остановки введите слово "stop".')
maximum = 0
max_number_sum = 0
while True:
    number = input('Введите натуральное число: ')
    if 'stop' != number:
        if number.isdigit():
            number = int(number)
            if number > 0:
                summa = 0
                temp = number
                while temp:
                    summa += temp % 10
                    temp //= 10
                if maximum < summa:
                    maximum = summa
                    max_number_sum = number
            else:
                print('Введите другое число')
        else:
            print('Это не число!')
    else:
        break
print(f'Среди натуральных чисел, которые были введены, {max_number_sum} наибольшее по сумме цифр = {maximum}')
