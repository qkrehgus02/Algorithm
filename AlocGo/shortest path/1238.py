import heapq

n, m, x = map(int, input().split())

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    INF = float('inf')
    weights = [INF] * (n+1)
    weights[start] = 0
    
    while heap:
        nw, node = heapq.heappop(heap)
        if(nw > weights[node]):
            continue
        
        for n1, w in graph[node]:
            newW = nw + w
            if weights[n1] > newW:
                weights[n1] = newW
                heapq.heappush(heap, [newW, n1])
    return weights
            

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append([end, time])

max = 0

come_back = dijkstra(x) #집으로 돌아오는 길
  
for i in range(1, n+1):
    if i == x: #자기자신은 어차피 0이니까 패스
        continue
    
    timegraph = dijkstra(i)
    if(timegraph[x] + come_back[i] > max):
        max = timegraph[x] + come_back[i]
    
print(max)