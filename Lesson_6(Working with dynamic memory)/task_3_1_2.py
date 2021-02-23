from memory_profiler import profile


def even(n, i):
    if n < i:
        return 0
    return 1 + even(n - i, i)


@profile
def even_num(n):
    ans = []
    for j in range(2, 10):
        ans.append(even(n, j))
    return ans
