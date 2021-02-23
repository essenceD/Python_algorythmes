# 3.
# Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

from collections import deque


def get_graph(n):
    return [[i for i in range(n) if i != j] for j in range(n)]


def go_deep(graph, start, finish):
    if start > len(graph) or finish > len(graph) or start < 0 or finish < 0:
        return f'Incorrect interval was input!'
    length = len(graph)
    parent = [None] * length
    is_visited = [False] * length
    deq = deque([start])
    is_visited[start] = True
    while len(deq) > 0:
        current = deq.pop()
        if current == finish:
            break
        for vertex in graph[current]:
            if not is_visited[vertex]:
                is_visited[vertex] = True
                parent[vertex] = current
                deq.appendleft(vertex)
    else:
        return 'You will never see this msg with graph where all vertexes connected to each other >:-)='
    cost = 0
    way = deque([finish])
    i = finish
    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]
    cost += 1
    way.appendleft(start)
    return list(way)


size = int(input('Number of vertexes: '))
st = int(input('Start vertex: '))
fin = int(input('Finish vertex: '))
g = get_graph(size)
print('Your graph (adjacency list):', *g, sep='\n')
print(f'The way is: {go_deep(g, st, fin)}')

# size = int(input('Number of vertexes: '))
# st = int(input('Start vertex: '))
# fin = int(input('Finish vertex: '))
# print(f'The way is: [{st}, {fin}]')
