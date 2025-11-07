from collections import deque

n, m = map(int, input().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(input()))

def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y))
    people = 0

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 'O': # 갈 수 있는 곳이라면
                    queue.append((nx, ny)) # 큐에 넣고 탐색
                    graph[ny][nx] = "X" # 방문 처리
                if graph[ny][nx] == 'P': # 사람을 만나면
                    people += 1 # 사람 수 증가
                    queue.append((nx, ny)) # 큐에 넣고 탐색
                    graph[ny][nx] = "X" # 방문 처리
    return people

for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            result = bfs(j, i, graph)
            
if result == 0:
    print("TT")
else:
    print(result)