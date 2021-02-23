# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint as rd

base = [rd(1, 20) for j in range(10)]
mirror = base[:]
minimal = []
mn = base[0]
while len(minimal) < 2:
    for i in base:
        if i < mn:
            mn = i
    minimal.append(base.pop(base.index(mn)))
    mn = base[0]
print(f'Original list: {mirror}\nTwo minimal values: {minimal}')
