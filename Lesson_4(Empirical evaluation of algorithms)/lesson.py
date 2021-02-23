import cProfile
def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# E:\ALGORITHMICS\Lesson_4>py -m timeit -n 1000 -s "import lesson" "lesson.fib(10)"
#test_fib(fib)
print(fib(10))
# cProfile.run('fib(10)')
# 177/1    0.000    0.000    0.000    0.000 lesson.py:9(fib)
# 1000 loops, best of 5: 12.4 usec per loop
