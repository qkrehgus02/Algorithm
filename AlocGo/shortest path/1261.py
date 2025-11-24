from collections import deque

m, n = map(int, input().split())

graph = [] #0은 빈 방, 1은 벽

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 100000000000

for _ in range(n):
    s = input().strip()
    graph.append(list(map(int, s)))
    
cost = [[INF for _ in range(m)] for _ in range(n)]
cost[0][0] = 0

#0-1 bfs(bfs + dijkstra)
#벽이 아닌 부분을 우선 탐색
#이후 벽을 만나면 탐색하며 cost를 갱신

deq = deque()
deq.append((0, 0))

while deq:
    x, y = deq.popleft()
    
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        
        if(0 <= px < n and 0 <= py < m ): #유효한 공간이거나 방문하지 않은 경우에만 탐색
            w = graph[px][py]
            new_cost = cost[x][y] + w
            
            if new_cost < cost[px][py]:
                cost[px][py] = new_cost
                
                if(graph[px][py] == 0): #빈 방을 만나면
                    deq.appendleft((px, py)) #덱의 앞쪽에 삽입
                else: #벽을 만나면
                    deq.append((px, py)) #덱의 뒷쪽에 삽입

print(cost[n-1][m-1])