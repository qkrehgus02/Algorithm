graph = []

for _ in range(9):
    graph.append(list(map(int, input())))

def search(x, y, num, graph):
    for i in range(9):
        if i == x:
            continue
        else:
            if graph[i][y] == num:
                return False
    for i in range(9):
        if i == y: 
            continue
        else:
            if graph[x][i] == num:
                return False
    bx, by = (x//3) * 3 , (y // 3) * 3
    for i in range(bx, bx + 3):
        for j in range(by, by + 3):
            if graph[i][j] == num and (i, j) != (x, y):
                return False
    return True

def solve(graph):
    for i in range(9):
        for j in range(9):
            if graph[i][j] == 0:
                for k in range(1, 10):
                    if search(i, j, k, graph) == True:
                        graph[i][j] = k
                        if solve(graph):
                            return True
                        graph[i][j] = 0
                return False
    return True 

solve(graph)

for i in graph:
    print(''.join(map(str, i)))
                    