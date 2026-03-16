from collections import deque

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def move_right(graph):
    result = []
    for i in range(n):
        temp = 0
        r = deque()
        for j in range(n-1, -1, -1):
            if temp == 0:
                temp = graph[i][j]
            else:
                if graph[i][j] == 0:
                    continue
                elif graph[i][j] == temp:
                    r.appendleft(temp*2)
                    temp = 0
                else:
                    r.appendleft(temp)
                    temp = graph[i][j]
        r.appendleft(temp)
        while len(r) < n:
            r.appendleft(0)
        result.append(list(r))
    return result

def move_left(graph):
    result = []
    for i in range(n):
        temp = 0
        r = []
        for j in range(n):
            if temp == 0:
                temp = graph[i][j]
            else:
                if graph[i][j] == 0:
                    continue
                elif graph[i][j] == temp:
                    r.append(temp*2)
                    temp = 0
                else:
                    r.append(temp)
                    temp = graph[i][j]
        r.append(temp)
        while len(r) < n:
            r.append(0)
        result.append(r)
    return result

def move_up(graph):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        temp = 0
        idx = 0
        for i in range(n):
            if temp == 0:
                temp = graph[i][j]
            else:
                if graph[i][j] == 0:
                    continue
                elif graph[i][j] == temp:
                    result[idx][j] = temp * 2
                    idx += 1
                    temp = 0
                else:
                    result[idx][j] = temp
                    idx += 1
                    temp = graph[i][j]
        if temp != 0:
            result[idx][j] = temp
    return result

def move_down(graph):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        temp = 0
        idx = n-1
        for i in range(n-1, -1, -1):
            if temp == 0:
                temp = graph[i][j]
            else:
                if graph[i][j] == 0:
                    continue
                elif graph[i][j] == temp:
                    result[idx][j] = temp * 2
                    idx -= 1
                    temp = 0
                else:
                    result[idx][j] = temp
                    idx -= 1
                    temp = graph[i][j]
        if temp != 0:
            result[idx][j] = temp
    return result

def search(graph, depth):
    if depth == 5:
        return max(max(row) for row in graph)
    
    result = 0
    for move in [move_up, move_down, move_left, move_right]:
        result = max(result, search(move(graph), depth + 1))
    
    return result 

print(search(graph, 0))
