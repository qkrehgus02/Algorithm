from collections import deque

n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input())))

def calculate_size(x, y, graph): #구역의 크기를 반환하는 bfs
    count = 0
    queue = deque()
    queue.append((x, y))
    graph[x][y] = -1 #시작 셀 방문처리

    while queue:
        nx, ny = queue.popleft()
        count += 1
        
        for i in range(4):
            px = nx + dx[i]
            py = ny + dy[i]
            if 0 <= px < n and 0 <= py < m:
                if graph[px][py] == 0:
                    queue.append((px, py))
                    graph[px][py] = -1 #방문처리
    
    return count

def set_size(x, y, graph, weight):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = weight #시작 셀 방문처리
    visited = set()
    
    while queue:
        nx, ny = queue.popleft()

        for i in range(4):
            px = nx + dx[i]
            py = ny + dy[i]
            if 0 <= px < n and 0 <= py < m:
                if graph[px][py] == -1:
                    queue.append((px, py))
                    graph[px][py] = weight #방문처리
                if graph[px][py] == -2 and (px, py) not in visited:
                    result[px][py] += weight
                    visited.add((px, py))
                    
        
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = -2
            result[i][j] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            weight = calculate_size(i, j, graph)
            set_size(i, j, graph, weight)                

for r in result:
    print(''.join(map(str, [x % 10 for x in r])))
    
#역으로 벽이 없는 곳을 탐색하여 구역의 크기를 설정
#특정 구역과 붙어있는 벽이 있다면 그 벽을 부수면 해당 구역에 접근 가능하다는 뜻
#따라서 특정 구역의 크기를 구하고, 구역과 붙어있는 벽에 그 구역의 크기를 더해주면 됨. 

