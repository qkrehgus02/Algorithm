import math
import heapq

n = int(input())

star = []
graph = [[0 for _ in range(n)] for _ in range(n)]
visited = [None for _ in range(n)]
heap = []

for i in range(n):
    x, y = map(float, input().split())
    star.append([x, y])
    
for i in range(n):
    for j in range(i, n):
        if i == j:
            graph[i][j] = 0
        else:
            k = math.sqrt((star[i][0] - star[j][0]) ** 2 + (star[i][1] - star[j][1]) ** 2)

            graph[i][j] = k 
            graph[j][i] = k

heapq.heappush(heap, (0, 0))

while heap:
    weight, node = heapq.heappop(heap)
    
    if visited[node] == None: #만약 방문하지 않았으면
        visited[node] = weight
        
        for i in range(n):
            if visited[i] == None:
                heapq.heappush(heap,(graph[node][i], i))
    
ans = 0 
for i in visited:
    ans += i

print(ans)