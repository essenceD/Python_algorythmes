# Закодируйте любую строку по алгоритму Хаффмана.
from collections import namedtuple
from operator import attrgetter

# My own recursion method:


def indexer(arr: list, value: str) -> str:

    if value in arr:
        return f'{arr.index(value)}'

    if (isinstance(arr[0], list) and isinstance(arr[1], str)) or (isinstance(arr[0], str) and isinstance(arr[1], list)):
        for j in arr:
            if isinstance(j, list):
                return f'{arr.index(j)} -> {indexer(j, value)}'

    if isinstance(arr[0], list) and isinstance(arr[1], list):

        sub_1 = f'{arr.index(arr[1])} -> {indexer(arr[1], value)}'
        sub_2 = f'{arr.index(arr[0])} -> {indexer(arr[0], value)}'
        if 'None' not in sub_1:
            return sub_1
        else:
            return sub_2


while True:
    a = input('Type any symbols to encode it by Haffman\'s method: ')
    if len(a) > 0:
        break
    else:
        print('Not blank please!')

e = list(sorted(set(a)))

d = []
Weight = namedtuple('Weight', 'ch fr')  # ch = char, fr = frequency

for i in e:
    d.append(Weight(i, a.count(i)))

d = sorted(d, key=attrgetter('fr'))
tree = []

while len(d) > 1:

    for i in d:
        print(f'{i.ch}  ->  {i.fr}')
    print('*' * 50)

    s_0 = d.pop(0)
    s_1 = d.pop(0)
    tree = [s_0.ch, s_1.ch]
    new_fr = s_0.fr + s_1.fr
    new_ch = tree
    idx = -1

    for i in range(len(d)):
        if d[i].fr > new_fr:
            idx = i
            break

    if idx == -1:
        d.append(Weight(new_ch, new_fr))
    else:
        d.insert(idx, Weight(new_ch, new_fr))

print(f'Tree: {tree}\n', '*' * 50, sep='')

for i in e:
    print(f'letter <{i}> address: {indexer(tree, i)}')
print('*' * 50, '\nEncoding table:')
codes = {_: indexer(tree, _).replace(' -> ', '') for _ in e}


for i in codes.keys():
    print(f'<{i}> = {codes[i]}')
print('*' * 50, '\nEncoded phrase:')

for i in a:
    print(i.replace(i, codes[i]), end=' ')
print()
