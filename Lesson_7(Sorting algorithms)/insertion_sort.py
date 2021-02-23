import random

size = 10
arr = [i for i in range(size)]
random.shuffle(arr)
print(arr)


def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam


insertion_sort(arr)
print(arr)
