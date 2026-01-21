#https://www.acmicpc.net/problem/13141

N, M = map(int, input().split())
INF = int(1e9)

graph = [[INF for _ in range(N)] for _ in range(N)]
shortest = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    S, E, L = map(int, input().split())
    S -= 1
    E -= 1
    if graph[S][E] == INF :
        graph[S][E] = L
        graph[E][S] = L
        shortest[S][E] = L
        shortest[E][S] = L
    elif shortest[S][E] > L: #기존에 값이 들어있고 L보다 크면
        shortest[S][E] = L
        shortest[E][S] = L
    elif graph[S][E] < L:
        graph[S][E] = L
        graph[E][S] = L
    
for i in range(N):
    shortest[i][i] = 0        

for k in range(N):
    for i in range(N):
        for j in range(N):
            shortest[i][j] = min(shortest[i][k] + shortest[k][j], shortest[i][j])

result = INF
        
for n in range(N): #시작정점 지정
    burn = 0
    for u in range(N): 
        for v in range(N): #한개의 간선에 대하여 
            if graph[u][v] != INF:
                temp = max(shortest[n][u], shortest[n][v]) + (graph[u][v] - abs(shortest[n][u] - shortest[n][v])) / 2
                if temp > burn:
                    burn = temp
    if burn < result:
        result = burn

print(f"{result:.1f}")