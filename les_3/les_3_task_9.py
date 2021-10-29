"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

size = 4
matrix = [[random.randint(0, 100) for _ in range(9)] for _ in range(7)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
min_column = [0] * len(matrix[0])
for j in range(len(matrix[0])):
    min_column[j] = matrix[0][j]
    for i, _ in enumerate(matrix):
        if min_column[j] > matrix[i][j]:
            min_column[j] = matrix[i][j]
print('-' * 5 * size)
print(*min_column)
print('-' * 5 * size)
maximum = min_column[0]
for el in min_column:
    if maximum < el:
        maximum = el
print(maximum)
