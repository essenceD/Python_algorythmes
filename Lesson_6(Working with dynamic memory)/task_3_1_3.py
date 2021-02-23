from memory_profiler import profile


@profile
def even_num(n):
    ans = (int(n / i) for i in range(2, 10))
    return ans
