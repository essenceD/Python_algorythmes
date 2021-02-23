# 1.
# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
import collections as cl

num_inc = int(input('Enter number of companies: '))
Corp = cl.namedtuple('Corp', 'name profit', rename=True)
stat = cl.deque()
for i in range(1, num_inc + 1):
    data = []
    name = input(f'Enter name of corporation {i}: ')
    data.append(name)
    profit = input(f'Enter year profit of corporation {name}: ')
    data.append(int(profit))
    stat.append(Corp(data[0], data[1]))
avg_profit = sum([i[1] for i in stat]) / len(stat)
below = []
above = []
for i in stat:
    if i[1] < avg_profit:
        below.append(i)
    else:
        above.append(i)
print(f'Average profit: {avg_profit}\nBelow avg profit:\n{below}\nAbove avg profit:\n{above}')
