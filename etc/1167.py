v = int(input())

graph = [[0 for _ in range(v)] for _ in range(v)]


from collections import deque

def bfs(start):
    visited = [False for _ in range(v)]
    
    queue = deque()
    queue.append((start, 0)) #시작 정점은 1번 정점 (1-1 = 0)
    visited[start] = True
    max_weight = 0
    max_point = start
    
    while queue:
        point, weight = queue.popleft()
        
        for i in range(len(graph[point])):
            if graph[point][i] != 0 and visited[i] == False:
                queue.append((i, weight + graph[point][i])) 
                visited[i] = True
                if(weight + graph[point][i] > max_weight):
                    max_weight = weight + graph[point][i]
                    max_point = i
                    
    
    return max_point, max_weight

for _ in range(v):
    s = list(map(int, input().split()))
    for i in range(1, len(s)-1 , 2):
        graph[s[0]-1][s[i]-1] = s[i+1]
        graph[s[i]-1][s[0]-1] = s[i+1]

edge_point, garbage = bfs(0)

garbage, ans = bfs(edge_point)

print(ans)