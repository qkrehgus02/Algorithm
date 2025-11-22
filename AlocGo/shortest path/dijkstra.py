import heapq 

#heap의 역할은 현재까지 비용이 가장 작은 노드를 탐색하기 위해서! 
#각 노드까지 최단 비용을 저장할 weight 배열 사용(dp 역할)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start]) #최소힙에 item에 배열을 넣게 되면 배열의 첫 요소가 heap 정렬의 기준
    INF = float('inf')
    weights = [INF] * (vertex+1)
    weights[start] = 0 
    
    while heap:
        weight, node = heapq.heappop(heap)
        if (weight > weights[node]): #heap에서 꺼냈을 때 해당 노드에 weight값 보다 크다 -> 최단 경로가 이미 정해진 노드이므로 무시하고 넘어감
            continue
        
        for n, w in graph[node]:  #인접한 노드를 탐색해서
            W = weight + w #현재까지 비용 + 간선 비용
            if weights[n] > W: # 반약 새로운 비용이 더 작으면
                weights[n] = W # 갱신!
                heapq.heappush(heap, (W, n)) #하고 힙에 넣음
    return weights
    
vertex, edge, start = map(int, input().split())
graph = [[] for _ in range(vertex+1)]
for i in range(vertex + edge):
    src, dst, weight = map(int, input().split())
    graph[src].append([dst, weight])
    
weights = dijkstra(start)
print(weights)