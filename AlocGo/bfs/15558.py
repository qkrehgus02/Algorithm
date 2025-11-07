n, k = map(int, input().split())

graph = []

dx = [1, -1, k, k]
dy = [0, 0, 1, -1]

for _ in range(2):
    graph.append(list(map(int, input())))

print(graph)