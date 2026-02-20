from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

anslist = []

for _ in range(t):
    h, w = map(int, input().split())
    graph = []
    ans = 0  #답을 나타내는 변수
    startpoint = [] #건물의 출입구 부분
    keylist = [] #현재까지 찾은 key를 저장
    flag = True

    for _ in range(h):
        graph.append(list(input()))

    temp = list(input())
    if temp[0] != '0':
        for t in temp:
            keylist.append(t)

    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1:
                if graph[i][j] != '*':
                    startpoint.append((i, j))

    def bfs():
        global flag, ans
        visited = [[False for _ in range(w)] for _ in range(h)] #방문처리
        flag = False #글로벌변수 flag는 bfs를 도는 순간 false처리
        queue = deque()

        for s in startpoint:
            if visited[s[0]][s[1]] == False: #방문하지 않은 시작점이 있다면

                queue.append((s[0], s[1]))

                while queue: #그 점부터 탐색 시작
                    x, y = queue.popleft()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    if 'A' <= graph[x][y] <= 'Z':
                        if graph[x][y].lower() not in keylist:
                            continue
                        graph[x][y] = '.'
                    if graph[x][y] == '$':
                        ans += 1
                        graph[x][y] = '.'
                    if 'a' <= graph[x][y] <= 'z':
                        if graph[x][y] not in keylist:
                            keylist.append(graph[x][y])
                            flag = True
                        graph[x][y] = '.'

                    for i in range(4):
                        px = x + dx[i]
                        py = y + dy[i]

                        if 0 <= px < h and 0 <= py < w:
                            if visited[px][py] == False and graph[px][py] != '*':
                                queue.append((px, py))
    while flag:
        bfs()

    anslist.append(ans)

for i in anslist:
    print(i)