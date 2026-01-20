from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []

def bfs(x, y, visited): # (x, y)는 이미 상대의 돌이라고 가정
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    count = 1
    flag = True
        
        
    while queue:
        nx, ny = queue.popleft() # 큐에서 값을 꺼낸다.

        for i in range(4): #4가지 방향에 대해서 탐색
            px = nx + dx[i]
            py = ny + dy[i]

            if 0 <= py < n and 0 <= px < m:
                if visited[py][px] == False:
                    if graph[py][px] == 0: #0을 만나면 돌을 먹을 수 없는 것
                        flag = False
                    elif graph[py][px] == 2: #2를 만나면 큐에 넣어 탐색을 이어나감.
                        queue.append((px, py))
                        visited[py][px] = True
                        count += 1
            #1인 경우는 그냥 아무것도 안하면 됨.
    if flag == True:
        return count
    else:
        return -1

def search():
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2 and visited[i][j] == False:
                c = bfs(j, i, visited)
                if c != -1:
                    count += c

    return count
   
n, m = map(int, input().split())

for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0 

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            for k in range(n):
                for h in range(m):
                    if graph[k][h] == 0:
                        graph[i][j] = 1 
                        graph[k][h] = 1
                        s = search()
                        graph[i][j] = 0
                        graph[k][h] = 0
                        if s > result:
                            result = s

print(result)
