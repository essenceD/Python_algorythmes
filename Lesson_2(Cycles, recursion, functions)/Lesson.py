import sys


def func(a, b):
    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'
    if a < b:
        return f'{a}, {func(a + 1, b)}'


def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))  # m > 0 n > 0


def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


def gcd2(m, n):
    if n == 0:
        return m
    return gcd2(n, m % n)


def gcd3(m, n):
    while n != 0:
        m, n = n, m % n
    return m


# sys.setrecursionlimit(3000)
# print(func(1, 10))
# print(akk(3, 8))
print(gcd3(12, 9))
