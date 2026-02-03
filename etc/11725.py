n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

from collections import deque

queue = deque()
queue.append(0)
visited = [False for _ in range(n)]
parent = [None for _ in range(n)]

while queue:
    node = queue.popleft()
    for g in graph[node]:
        if visited[g] == False:
            parent[g] = node + 1
            queue.append(g)
            visited[g] = True

for i in range(1, len(parent)):
    print(parent[i])