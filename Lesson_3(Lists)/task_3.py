# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint as rd

base = [rd(1, 99) for j in range(10)]
mx = base[0]
mn = base[0]
for i in base:
    if i > mx:
        mx = i
    if i < mn:
        mn = i
print('Original list:', end=' ')
for i in base:
    print(f'{i:<4}', end='')
imn = base.index(mn)
imx = base.index(mx)
base[imn], base[imx] = base[imx], base[imn]
print('\nModified list:', end=' ')
for i in base:
    print(f'{i:<4}', end='')
print(f'\nmax={mx} array[{imx}]; min={mn} array[{imn}]')
