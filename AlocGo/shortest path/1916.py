import heapq

n = int(input())
m = int(input())

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    INF = float('inf')
    weights = [INF] * (n+1)
    weights[start] = 0 
    
    while heap:
        weight, node = heapq.heappop(heap)
        if(weight > weights[node]):
            continue
        
        for nxt, w in graph[node]:
            W = weight + w
            if weights[nxt] > W:
                weights[nxt] = W 
                heapq.heappush(heap, (W, nxt))
    return weights

graph = [[]for _ in range(n+1)]

for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))

start, end = map(int, input().split())  

weights = dijkstra(start)
print(weights[end])