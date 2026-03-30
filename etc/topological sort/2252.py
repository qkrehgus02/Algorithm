from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]

ans = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

queue = deque()

for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    ans.append(node)
    
    for i in graph[node]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

for a in ans:
    print(a, end = " ")