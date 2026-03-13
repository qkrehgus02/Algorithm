n = int(input())
m = int(input())

INF = 10**16

graph = [[INF for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print("")