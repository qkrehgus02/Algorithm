import heapq
INF = 10**18

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dist = [INF for _ in range(n+1)]
    dist[start] = 0
    
    while heap:
        weight, node = heapq.heappop(heap)
        
        if weight > dist[node]:
            continue
            
        for next, w in graph[node]:
            W = weight + w 
            if dist[next] > W:
                dist[next] = W
                heapq.heappush(heap, (W, next))
    return dist

def wolf(start):
    heap = []
    # 0: 이번 이동이 빠름, 1: 이번 이동이 느림
    heapq.heappush(heap, (0, start, 0))
    
    dist = [[INF for _ in range(n+1)] for _ in range(2)]
    dist[0][start] = 0
    
    while heap:
        weight, node, state = heapq.heappop(heap)
        
        if weight > dist[state][node]:
            continue
        
        for nxt, w in graph[node]:
            if state == 0:   
                W = weight + w // 2
                next_state = 1
            else:            
                W = weight + 2 * w
                next_state = 0
            
            if W < dist[next_state][nxt]:
                dist[next_state][nxt] = W
                heapq.heappush(heap, (W, nxt, next_state))
                
    return dist

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append([b, d*2])
    graph[b].append([a, d*2])
    
fox = dijkstra(1)
wolf_dist = wolf(1)

count = 0
for i in range(2, n+1):
    if fox[i] < min(wolf_dist[0][i], wolf_dist[1][i]):
        count += 1
  
print(count)