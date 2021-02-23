from memory_profiler import profile


@profile
def even_num(n):
    ans = {i + 2: [j for j in range(2, n) if j % (i + 2) == 0] for i in range(8)}
    return ans
