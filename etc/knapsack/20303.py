from collections import deque

N, M, K = map(int, input().split())

candy = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

group_list = []

def grouping(i):
    queue = deque()
    queue.append(i)
    visited[i] = True
    weight = 0
    size = 0
    
    while queue:
        node = queue.popleft()
        weight += candy[node-1]
        size += 1
        
        for n in graph[node]:
            if visited[n] == False:
                queue.append(n)
                visited[n] = True
    
    return (weight, size)

for i in range(1, N+1):
    if visited[i] == False:
        group_list.append(grouping(i))

dp = [0 for _ in range(K)]

for weight, size in group_list:
    for j in range(K-1, size-1, -1):
        dp[j] = max(dp[j], dp[j-size] + weight)
        
print(dp[K-1])