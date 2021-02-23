from collections import deque
from random import randint as rd

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')
b = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)
print(b, c, sep='\n')
c.clear()
print(c)
print('*' * 50)
d = deque([i for i in range(5)], maxlen=7)
d.append(5)
d.appendleft(6)
print(d)
d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)
# deque([6, 0, 1, 2, 3, 4, 5])
# deque([12, 11, 10, 6, 0, 1, 2, 3, 4, 5, 7, 8, 9])
# maxlen=7
# deque([6, 0, 1, 2, 3, 4, 5], maxlen=7)
# deque([12, 11, 10, 2, 3, 4, 5], maxlen=7)
print('*' * 50)
f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')
print('*' * 50)
g = deque([i for i in range(5)], maxlen=7)
print(g.count(2))
print(g.index(3))
g.insert(2, 6)
print(g)
g.reverse()
print(g)
g.rotate(3)
print(g)

arr = [rd(-100, 100) for i in range(10)]
print(arr)
deq = deque()
for i in arr:
    if i < 0:
        deq.appendleft(i)
    elif i > 0:
        deq.append(i)
print(deq)
print('*' * 50)
last_three = deque(deq, 3)
print(last_three)









