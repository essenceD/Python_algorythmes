import random

size = 10
arr = [i for i in range(size)]
random.shuffle(arr)
print(arr)


def revers(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]


revers(arr)
print(arr)

arr.reverse()
print(arr)

arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

print('*' * 50)
t = tuple(random.randint(0, 100) for _ in range(size))
print(t)
t = tuple(sorted(t))
print(t)
t = tuple(sorted(t, reverse=True))
print(t)
