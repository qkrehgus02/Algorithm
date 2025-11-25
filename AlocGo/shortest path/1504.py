N, E = map(int, input().split())

INF = 10000000

graph = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

v1, v2 = map(int, input().split())

#Floyd
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans1 = graph[0][v1-1] + graph[v1-1][v2-1] + graph[v2-1][N-1]
ans2 = graph[0][v2-1] + graph[v2-1][v1-1] + graph[v1-1][N-1]

ans = min(ans1, ans2)

if ans >= INF:
    print(-1)
else:
    print(ans)