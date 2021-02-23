from random import randint as rd


def bin_search(arr, val):
    left = 0
    right = len(arr) - 1
    pos = len(arr) // 2

    while arr[pos] != val and left <= right:
        if val > arr[pos]:
            left = pos + 1
        else:
            right = pos - 1
        pos = (left + right) // 2
    return -1 if left > right else pos


a = [rd(0, 1000) for i in range(100)]
a.sort()
print(a)
n = int(input('what to find? '))
print(bin_search(a, n))
