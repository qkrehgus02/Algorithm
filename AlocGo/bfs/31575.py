from collections import deque

def bfs(x, y, graph): #탐색 함수
    queue = deque()
    queue.append((x, y))
    
    while queue: #큐가 빌 때까지 반복
        nx , ny = queue.popleft() #1. 큐에서 꺼내고
        
        for i in range(2): #이동 가능한 방향으로 탐색
            px = nx + dx[i]
            py = ny + dy[i]
            
            if(0 <= px < n and 0 <= py < m): #3. 그래프 밖을 벗어나지 않는다면
                if(graph[py][px] == 1): #4. 그리고 이동할 수 있고, 아직 지나오지 않은 곳이라면
                    graph[py][px] = 2 #해당 위치 방문처리
                    queue.append((px, py)) # 5. 큐에 넣는다

n, m = map(int, input().split())

graph = []

dx = [1, 0]
dy = [0, 1]
#문제 조건에 동쪽, 남쪽으로만 이동 가능하다고 되어있음 !! 

for _ in range(m):
    graph.append(list(map(int, input().split())))

#조건 1. 시작점은 북서쪽 끝 
#조건 2. 왼쪽 위 끝칸은 무조건 1
# -> 무조건 시작점은 (0, 0)
 
bfs(0, 0, graph) #시작점 기준으로 탐색 돌리고

if (m==1 and n ==1):
    print("Yes")
else:
    if(graph[m-1][n-1] == 1): #해당 위치가 방문되지 않았다면
        print("No") #못 감
    else: #아니면
        print("Yes") #갈 수 있음
