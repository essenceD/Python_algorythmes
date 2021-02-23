# 4.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

def next_x(lim, x=1):
    ans = x
    if lim > 1:
        ans += next_x(lim-1, x=x/(-2))
    return ans


steps = int(input('Enter number of steps: '))
print(next_x(steps))
