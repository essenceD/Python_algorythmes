# 2.
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import randint as rd


def merge(left, right):
    sorted_list = []
    idx_left = 0
    idx_right = 0
    left_length, right_length = len(left), len(right)
    for _ in range(left_length + right_length):
        if idx_left < left_length and idx_right < right_length:
            if left[idx_left] <= right[idx_right]:
                sorted_list.append(left[idx_left])
                idx_left += 1
            else:
                sorted_list.append(right[idx_right])
                idx_right += 1
        elif idx_left == left_length:
            sorted_list.append(right[idx_right])
            idx_right += 1
        elif idx_right == right_length:
            sorted_list.append(left[idx_left])
            idx_left += 1
    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left_list = merge_sort(nums[:middle])
    right_list = merge_sort(nums[middle:])
    return merge(left_list, right_list)


size = 10
arr = [rd(0, 49) for _ in range(size)]
new_arr = merge_sort(arr)
print(f'Initial array: {arr}\nSorted  array: {new_arr}')
