from collections import deque

graph = []
for _ in range(5):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    visited = [[False for _ in range(5)] for _ in range(5)]
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    count = 1
    
    while queue:
        nx, ny = queue.popleft()
        
        for i in range(4):
            px = nx + dx[i]
            py = ny + dy[i]
            
            if 0 <= px < 5 and 0 <= py < 5:
                if visited[px][py] == False and graph[px][py] == '*':
                    queue.append((px, py))
                    visited[px][py] = True
                    count += 1
    if count == 5:
        return True
    else:
        return False
    
def search():
    for i in range(5):
        for j in range(5):
            if graph[i][j] == '*':
                return bfs(i, j)