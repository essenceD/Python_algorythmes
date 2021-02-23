# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint as rd

rows, cols = 5, 6
min_cols = []
matrix = [[rd(1, 99) for i in range(cols)] for j in range(rows)]
print(f'Original matrix {rows}x{cols}:')
for i in matrix:
    for j in i:
        print(f'{j:<4}', end='')
    print()
for j in range(len(matrix[0])):
    mn = matrix[0][j]
    for i in range(len(matrix)):
        if matrix[i][j] < mn:
            mn = matrix[i][j]
    min_cols.append(mn)
print('\nMinimal values by columns:')
max_el = min_cols[0]
for i in min_cols:
    if i > max_el:
        max_el = i
    print(f'{i:<4}', end='')
print(f'\nMax from them is "{max_el}"')
