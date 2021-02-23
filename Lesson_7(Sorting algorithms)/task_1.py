# 1.
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint as rd


# bubble_sort: 1000 loops, best of 5: 437 usec per loop
def bubble_sort(array):
    for n in range(len(array) - 1):
        for i in range(len(array) - n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


# bubble_sort_basic: 1000 loops, best of 5: 675 usec per loop
def bubble_sort_basic(array):
    n = 1
    while n < len(arr):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


size = 100
arr = [rd(-100, 99) for _ in range(size)]
print(f'Initial array: {arr}')
bubble_sort(arr)
print(f'Sorted  array: {arr}')
