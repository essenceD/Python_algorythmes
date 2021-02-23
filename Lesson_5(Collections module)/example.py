from collections import OrderedDict, defaultdict, deque

n = 3000
with open('big_log.txt', 'r', encoding='utf-8') as file_r:
    log = deque(file_r, n)
data = OrderedDict()
spam = defaultdict(int)
for i in log:
    ip = i[:-1]
    if not ip.startswith('192.168'):
        spam[ip] += 1
        data[ip] = 1
print(spam)
print(data)
data.update(spam)
print(data)
with open('data.txt', 'w', encoding='utf-8') as file_w:
    for key, value in data.items():
        print(f'{key} - {value}', file=file_w)
