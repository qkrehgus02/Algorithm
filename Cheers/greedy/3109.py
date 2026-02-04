r, c = map(int, input().split())
graph = []

pipe = [-1, 0, 1] #파이프 우선순위
#가로축으로는 무조건 1씩 움직이니까 필요없음. 

for _ in range(r):
    graph.append(list(input()))

count = 0

def dfs(x, y):
    
    for i in range(3):
        nx = x + 1
        ny = y + pipe[i]
        
        if nx == c -1 and 0 <= ny < r and graph[ny][nx] == '.':
            graph[ny][nx] = count
            return True
        
        if 0 <= nx < c and 0 <= ny < r:
            if graph[ny][nx] == '.':
                graph[ny][nx] = count
                if dfs(nx, ny) == True:
                    return True
    return False

for i in range(r):
    graph[i][0] = count
    find = dfs(0, i)
    if find == True:
        count += 1
        
print(count)
