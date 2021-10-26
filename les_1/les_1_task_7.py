"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.

В соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100,
а также если он кратен 400.
"""
print('Введите год.')
year = int(input('Год - '))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Високосный год')
else:
    print('Обычный год')