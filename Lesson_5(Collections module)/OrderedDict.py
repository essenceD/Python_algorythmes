from collections import OrderedDict

a = {'cat': 5, 'dog': 2, 'mouse': 4}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)
b = {'cat': 5, 'dog': 2, 'mouse': 4}
new_b = OrderedDict(sorted(b.items(), key=lambda x: x[1]))
print(new_b)
print(new_b == new_a)
print('*' * 50)
new_b.move_to_end('mouse', last=True)
print(new_b)













