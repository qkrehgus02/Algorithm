from collections import deque
from itertools import permutations, product

graph = []
for _ in range(5):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, temp):
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
                if visited[px][py] == False and temp[px][py] == '*':
                    queue.append((px, py))
                    visited[px][py] = True
                    count += 1
    if count == piececount:
        return True
    else:
        return False

def search(temp):
    for i in range(5):
        for j in range(5):
            if temp[i][j] == '*':
                return bfs(i, j, temp)

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

piece = []
piececount = 0

for i in range(5):
    for j in range(5):
        if graph[i][j] == '*':
            piece.append((i, j))
            piececount += 1



coords = list(product(range(5), repeat=2))

min = 10000000000000

# 시작부터 연결되어 있으면 0 출력
if search(graph):
    print(0)
    exit()

for selected in permutations(coords, piececount):
    # 임시 그래프 생성
    temp = [['.' for _ in range(5)] for _ in range(5)]
    for x, y in selected:
        temp[x][y] = '*'

    if not search(temp):
        continue

    count = 0
    for i in range(piececount):
        a, b = selected[i]
        c, d = piece[i]
        count += manhattan(a, b, c, d)
    if count < min:
        min = count

print(min)
