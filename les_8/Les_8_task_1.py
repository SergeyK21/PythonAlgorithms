"""
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

n = int(input('Введите кол-во друзей: '))

graph = []
for i in range(n):
    vertex = [1] * n
    for j in range(n):
        if i == j:
            vertex[j] = 0
    graph.append(vertex)
print(*graph, sep='\n')

count = 0
for i in range(n):
    for j in range(i, n):
        count += graph[i][j]
print(f'Кол-во рукопожатий: {count}')
