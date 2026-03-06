import heapq

T = int(input())
INF = 10**16
real_result = []

def dijkstra(start):
    heap = []
    visited = [False for _ in range(n+1)]
    dist = [INF for _ in range(n+1)]
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    
    while heap:
        weight, node = heapq.heappop(heap)
        
        if visited[node] == False:
            visited[node] = True
            
            for i in graph[node]:
                nxt, w = i
                if dist[nxt] > weight + w:
                    dist[nxt] = weight + w
                    heapq.heappush(heap, (dist[nxt], nxt))
    return dist

for _ in range(T):
    gh_weight = INF
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    destination = []
    
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d]) #양방향 도로
        if (a == g and b == h) or (a == h and b == g):
            gh_weight = d
        
    for _ in range(t):
        destination.append(int(input()))
    
    destination.sort()
    distS = dijkstra(s)
    distG = dijkstra(g)
    distH = dijkstra(h)
    result = []
    
    for d in destination:
        flag = False
        if distS[g] + distH[d] + gh_weight == distS[d]:
            flag = True
        elif distS[h] + distG[d] + gh_weight == distS[d]:
            flag = True
        
        if flag == True:
            result.append(d)
       
    real_result.append(result)
    
for r in real_result:
    for k in r:
        print(k, end = " ")   
    print("")
    

