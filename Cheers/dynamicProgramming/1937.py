from collections import deque


n = int(input())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
#1 그래프를 탐색하며 가리키는 방향을 체크 
degree = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(4):
            cx = i + dx[k]
            cy = j + dy[k]
            if 0 <= cx < n and 0 <= cy < n:
                if graph[cx][cy] < graph[i][j]:
                    degree[i][j] += 1


queue = deque()



    
#2 DFS로 
for i in range(n):
    for j in range(n):
        if degree[i][j] == 0:
            queue.append((i, j))
            
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > graph[x][y]:
                    dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)
                    degree[nx][ny] -= 1
                    if degree[nx][ny] == 0:
                        queue.append((nx, ny))
print(max(max(row) for row in dp)+1)
