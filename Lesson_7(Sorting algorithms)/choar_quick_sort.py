import random

size = 10
arr = [i for i in range(size)]
random.shuffle(arr)
print(arr)


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []

    for item in array:
        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('The unexpected happened...')
    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)


new_arr = quick_sort(arr)
print(new_arr)


def quick_sort_no_memory(array, fst, lst):
    if fst >= lst:
        return
    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        array[i], array[j] = array[j], array[i]
        i, j = i + 1, j - 1
        quick_sort_no_memory(array, fst, j)
        quick_sort_no_memory(array, i, lst)


print(arr)
quick_sort_no_memory(arr, 0, len(arr) - 1)
print(arr)
