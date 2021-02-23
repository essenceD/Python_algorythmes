from collections import ChainMap


d_1 = {i: [2, 4, 6]['abc'.index(i)] for i in 'abc'}
d_2 = {i: [10, 20, 40]['abd'.index(i)] for i in 'abd'}
print(d_1, d_2, sep='\n')
d_map = ChainMap(d_1, d_2)
print(d_map)
d_2['a'] = 100
print(d_map)
print(d_map['a'])
print(d_map['d'])
print('*' * 50)
x = d_map.new_child({i: [111, 222, 333, 444]['abcd'.index(i)] for i in 'abcd'})
print(x)
print(x.maps[0])
print(x.maps[-1])
print(x.parents)
print('*' * 50)
y = d_map.new_child()
print(y)
print(y['a'])
y['a'] = 1
print(y)
print(list(y))
print(list(y.values()))



