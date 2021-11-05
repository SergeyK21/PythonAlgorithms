"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple, deque

Company = namedtuple('Company', 'name profit')
quantity_deque = deque()
print(quantity_deque)
quantity = int(input('Введите кол-во предприятий: '))
summa_profit = 0
for i in range(quantity):
    print()
    name = input(f'Введите название {i + 1}й организации: ')
    profit = float(input(f'Введите прибыль {i + 1}й компании: '))
    quantity_deque.append(Company(name, profit))
    summa_profit += profit
average_profit = summa_profit / len(quantity_deque)
less_average_profit = []
more_average_profit = []
for el in quantity_deque:
    if el.profit < average_profit:
        less_average_profit.append(el.name)
    else:
        more_average_profit.append(el.name)

print(f'Средняя прибыль = {average_profit}')
print(f'Предприятия у которых прибыль выше средней: {more_average_profit}')
print(f'Предприятия у которых прибыль ниже средней: {less_average_profit}')
