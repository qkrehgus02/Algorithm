from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
result = []

for _ in range(m):
    order = list(map(int, input().split()))
    for i in range(1, len(order) - 1):
        graph[order[i]].append(order[i+1])
        degree[order[i+1]] += 1

queue = deque()

for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    result.append(node)
    for n in graph[node]:
        degree[n] -= 1
        if degree[n] == 0:
            queue.append(n)

flag = True 
for d in degree:
    if d != 0:
        flag = False

if flag == False:
    print(0)
else:
    for r in result:
        print(r)