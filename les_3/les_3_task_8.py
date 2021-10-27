"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""
import random

size = 4
matrix = [[random.randint(0, 10) for _ in range(size)] for _ in range(size)]
matrix.append([0, 0, 0, 0])
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
print('-' * size * 5)
for i in range(size):
    for j, item in enumerate(matrix[i]):
        matrix[size][j] += item
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
