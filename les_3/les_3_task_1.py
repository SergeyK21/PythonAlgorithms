"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.
"""
result = [[], [], [], [], [], [], [], []]
for i in range(2, 100):
    if i % 2 == 0:
        result[0].append(i)
    if i % 3 == 0:
        result[1].append(i)
    if i % 4 == 0:
        result[2].append(i)
    if i % 5 == 0:
        result[3].append(i)
    if i % 6 == 0:
        result[4].append(i)
    if i % 7 == 0:
        result[5].append(i)
    if i % 8 == 0:
        result[6].append(i)
    if i % 9 == 0:
        result[7].append(i)
for i, el in enumerate(result, 2):
    print(f'Кратные {i} - {el}')
