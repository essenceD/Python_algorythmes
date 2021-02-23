import random

size = 10
arr = [i for i in range(size)]
random.shuffle(arr)
print(arr)


def shell_sort(array):
    assert len(array) < 4000, 'Too large array. Use different sort.'

    def new_increment(array_2):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(array_2) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, - increment):
                if arr[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]


shell_sort(arr)
print(arr)
