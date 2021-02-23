import random


def speed_sort():
    size = 100
    arr = [i for i in range(size)]
    random.shuffle(arr)

    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1

