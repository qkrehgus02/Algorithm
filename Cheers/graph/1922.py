import heapq

n = int(input())
m = int(input())

#INF = 10000000000

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    
    graph[a].append([b, c])
    graph[b].append([a, c])
    
#모든 컴퓨터를 연결하는 최소비용 -> MST를 구하라는 말과 동일

visited = [None for _ in range(n+1)]
heap = []
heapq.heappush(heap, (0, 1))
#a->a로 가는 경로가 있다고 해도 어차피 최소비용이므로 제거될 것임. 

while heap:
    weight, node = heapq.heappop(heap)
    
    if visited[node] == None: #방문하지 않았으면
        visited[node] = weight
    
        for next in graph[node]:
            nextnode = next[0]
            nextw = next[1]
            
            if graph[nextnode] != None:
                heapq.heappush(heap, (nextw, nextnode))
                
ans = 0

for i in visited:
    if i != None:
        ans += i

print(ans)