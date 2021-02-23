graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]
print(*graph, sep='\n')
print('*' * 50)
graph2 = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]
print(*graph2, sep='\n')
print('*' * 50)
graph2[0][1:3] = [2, 3]
graph2[1][2] = 2
graph2[2][1] = 2
print(*graph2, sep='\n')
