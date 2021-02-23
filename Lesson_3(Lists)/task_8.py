# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix, row = [], []
rows, cols, _sum = 4, 5, 0
for i in range(cols):
    for j in range(rows):
        if j == rows - 1:
            row.append(_sum)
            _sum = 0
        else:
            a = int(input())
            row.append(a)
            _sum += a
    matrix.append(row)
    row = []

for i in matrix:
    for j in i:
        print(f'{j:<4}', end='')
    print()
