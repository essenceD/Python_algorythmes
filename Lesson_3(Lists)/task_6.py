# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint as rd

base = [rd(1, 20) for j in range(10)]
mx = base[0]
mn = base[0]
res = 0
for i in base:
    if i > mx:
        mx = i
    if i < mn:
        mn = i
imn = base.index(mn)
imx = base.index(mx)
if imn - imx > 1:
    for i in base[imx + 1:imn]:
        res += i
    print(f'Original list: {base}\nmax={mx}, min={mn}\n"Between" list: {base[imx + 1:imn]}\n'
          f'Sum between MAX and MIN: {res}')
elif imx - imn > 1:
    for i in base[imn + 1:imx]:
        res += i
    print(f'Original list: {base}\nmax={mx}, min={mn}\n"Between" list: {base[imn + 1:imx]}\n'
          f'Sum between MAX and MIN: {res}')
else:
    print(f'{base}\nmax={mx}, min={mn}\nMAX and MIN are adjacent values!\nUnable to calculate sum.')
