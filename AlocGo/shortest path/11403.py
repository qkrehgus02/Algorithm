n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

#floyd
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
            
for i in range(n):
    print(*graph[i])