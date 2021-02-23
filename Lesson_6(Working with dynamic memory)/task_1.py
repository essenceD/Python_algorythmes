# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде
# комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.


# ------------------------------------------------!!!! NOTICE !!!!------------------------------------------------------

# !!!!!!!!!!!!!
# Чтобы получить правильные результаты, установите себе модуль memory-profiler, в нем находится декоратор @profile
# !!!!!!!!!!!!!

# ---------------------------------------------------- RESULTS ---------------------------------------------------------
# System INFO:
# Python ver.: ~3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]~
# System ver: ~win32~
#
# Рассчитывал сколько памяти занимает результат выполнения 1 задачи 3 урока.
# Оказалось, что вариант не самый удачный, потому что отличается только вариант хранения ответа.
# Если использовать декоратор @profile или возвращать в каждой функции результат суммирования getsizeof(),
# то результат был бы точнее.
# {'Func t1': 'Memory = 808', 'Func t2': 'Memory = 344', 'Func t3': 'Memory = 344'}
# НО, установив memory-profiler и используя @profile мы увидим, что самое крутое решение под номером 3.
# ------------------------------------------------------- ВЫВОД --------------------------------------------------------
# Определенно, третий вариант с кортежем занимает меньше всего места. Значит, он лучше всего.
# Кстати, если его проверить еще и тестом на скорость, то он тоже будет самый быстрый.

# INFO:
# Python ver.: ~3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]~
# System ver: ~win32~
# Filename: E:\ALGORITHMICS\Lesson_6\task_3_1_1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      4     18.9 MiB     18.9 MiB           1   @memory_profiler.profile
#      5                                         def even_num(n):
#      6     18.9 MiB      0.0 MiB         803       ans = {i + 2: [j for j in range(2, n) if j % (i + 2) == 0] for i in range(8)}
#      7     18.9 MiB      0.0 MiB           1       return ans
#
#
# Filename: E:\ALGORITHMICS\Lesson_6\task_3_1_2.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     10     18.9 MiB     18.9 MiB           1   @memory_profiler.profile
#     11                                         def even_num(n):
#     12     18.9 MiB      0.0 MiB           1       ans = []
#     13     18.9 MiB      0.0 MiB           9       for j in range(2, 10):
#     14     18.9 MiB      0.0 MiB           8           ans.append(even(n, j))
#     15     18.9 MiB      0.0 MiB           1       return ans
#
#
# Filename: E:\ALGORITHMICS\Lesson_6\task_3_1_3.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      4     18.9 MiB     18.9 MiB           1   @memory_profiler.profile
#      5                                         def even_num(n):
#      6     18.9 MiB      0.0 MiB           1       ans = (int(n / i) for i in range(2, 10))
#      7     18.9 MiB      0.0 MiB           1       return ans
#
# ans memory takes:
# {'Func t1': 'Memory = 808', 'Func t2': 'Memory = 344', 'Func t3': 'Memory = 336'}
#
# Process finished with exit code 0


# импорты серые потому что eval в коде.
import task_3_1_1 as t1
import task_3_1_2 as t2
import task_3_1_3 as t3
import sys


def calc_size(x):
    result = 0
    result += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                result += sys.getsizeof(xx)
        elif not isinstance(x, str):
            for xx in x:
                result += sys.getsizeof(xx)
        elif not isinstance(x, list):
            for xx in x:
                result += sys.getsizeof(xx)
    return result


print(f'INFO:\nPython ver.: ~{sys.version}~\nSystem ver: ~{sys.platform}~')
tasks = ['t1', 't2', 't3']
results = {f'Func {i}': f"Memory = {eval(f'calc_size({i}.even_num(99))')}" for i in tasks}
print(f'ans memory takes: \n{results}')
