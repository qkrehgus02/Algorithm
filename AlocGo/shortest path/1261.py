from collections import deque

m, n = map(int, input().split())

graph = [] #0은 빈 방, 1은 벽

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    s = input().strip()
    graph.append(list(map(int, s)))
    

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
    

print(graph)