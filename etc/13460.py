n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))

bx, by, rx, ry = 0, 0, 0, 0

for i in range(n): #초기 좌표 세팅
    for j in range(m):
        if graph[i][j] == 'B':
            bx = j
            by = i
        if graph[i][j] == 'R':
            rx = j
            ry = i

print(bx, by, rx, ry)
def up(graph):
    global rx, ry, bx, by
    
    if by <= ry: #B가 더 위일때
        #b 먼저 이동
        ny = by
        while True:
            if graph[ny][bx] == '#':
                break
            ny -= 1
        graph[by][bx] = '.'
        by = ny + 1
        graph[by][bx] = 'B'
        
        ny = ry
        while True:
            if graph[ny][rx] == '#' or graph[ny][rx] == 'B':
                break
            ny -= 1
        graph[ry][rx] = '.'
        ry = ny + 1 
        graph[ry][rx] = 'R'
    
    return graph

print(graph)
print(up(graph))