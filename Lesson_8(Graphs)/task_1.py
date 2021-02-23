# 1.
# На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

# short solution:
n = int(input('Enter number of friends: '))
g = [[1 if __ != _ else 0 for __ in range(n)] for _ in range(n)]
print('Your graph (adjacency matrix):', *g, f'Total handshakes: {sum([sum(_) for _ in g])}', sep='\n')

# detailed solution:
# def handshakes(graph):
#     shaked = [[False if __ == 0 else None for __ in _] for _ in graph]
#     print('Before handshaking:', *shaked, sep='\n')
#     total_hs = 0
#     for i in shaked[:]:
#         for j in i:
#             if j is None:
#                 total_hs += 1
#                 shaked[shaked[:].index(i)][i.index(j)] = True
#     print('After handshaking:', *shaked, sep='\n')
#     return total_hs
#
#
# n = int(input('Enter number of friends: '))
# g = [[1 if __ != _ else 0 for __ in range(n)] for _ in range(n)]
# print(f'Total handshakes: {handshakes(g)}')
