import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1
    
heap = []

for i in range(1, n+1):
    if degree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    r = heapq.heappop(heap)
    result.append(r)
    
    for i in graph[r]: 
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(heap, i)

for r in result:
    print(r, end=" ")