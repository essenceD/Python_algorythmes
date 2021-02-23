# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint as rd

base = [rd(1, 4) for j in range(10)]
cmx = base.count(base[0])
mx = base[0]
for i in base:
    c = base.count(i)
    if c > cmx:
        cmx = c
        mx = i
print(f'Base list: {base}\nThe most common number is "{mx}", it was dropped out {cmx} times.')
