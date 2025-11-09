from collections import deque

n, k = map(int, input().split())

graph = []

dx = [1, -1, k, k]
dy = [0, 0, 1, -1]

is_win = False

for _ in range(2):
    graph.append(list(map(int, input())))

def bfs(que, second):
    queue = deque(que)
    next_queue = deque()
    
    global is_win
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            
            if px >= n:
                is_win = True
                break
            
            if 0 <= px < n and 0 <= py < 2 and px > second:
                if graph[py][px] == 1:
                    graph[py][px] = 2 #방문처리하고
                    next_queue.append((px, py)) #temp에 넣기
    return next_queue

temp = deque()
temp.append((0, 0))

second = 0

while temp:                    
    temp = bfs(temp, second)
    second += 1
    for i in range(2):
        graph[i][second - 1] = 0 #이제 못 가는 길                 

if is_win == True:
    print("1")
else:
    print("0")