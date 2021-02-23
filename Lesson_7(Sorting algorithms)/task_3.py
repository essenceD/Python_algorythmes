# 3.
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint as rd


def get_med(array):
    min_val = array[0]
    max_val = array[0]
    for i in array:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    for i in array:
        min_counter = 0
        max_counter = 0
        median = i
        for j in array:
            if j < median:
                min_counter += 1
            if j > median:
                max_counter += 1
        if max_counter == min_counter:
            return median


n = int(input('Enter N = ')) * 2 + 1
arr = [rd(1, 1000) for _ in range(n)]
print(f'Initial array: {arr}\nMedian is: {get_med(arr)}')
print('*' * 50, 'self-control:', '*' * 50)
print(f'Initial array: {arr}\n'
      f'Sorted  array: {sorted(arr)}\n'
      f'Median is: {get_med(arr)} position is [{sorted(arr).index(get_med(arr)) + 1}] of [{len(arr)}]')
