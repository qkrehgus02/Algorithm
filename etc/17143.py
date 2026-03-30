R, C, M = map(int, input().split())

graph = [[-1 for _ in range(C+1)] for _ in range(R+1)]
shark = []

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r][c] = i #i는 상어의 번호
    shark.append([r, c, s, d, z, True]) #shark[상어번호][2-속력, 3-방향, 4-크기, 5-살아있는 상어인지]
    
def move(): #상어들을 이동시키는 칸
    for r in range(1, R+1): #기존 graph 초기화
        for c in range(1, C+1):
            graph[r][c] = -1
    for i in range(M):
        if shark[i][5] == True: #상어가 살아있다면
            r = shark[i][0]
            c = shark[i][1]
            if shark[i][3] == 1: #위로 움직여야한다면
                r -= shark[i][2] % (2*(R-1))
                if r < 1:
                    shark[i][3] = 2
                    r = 2 - r
                    if r > R:
                        shark[i][3] = 1
                        r = 2*R - r
            elif shark[i][3] == 2: #아래로 움직여야한다면
                r += shark[i][2] % (2*(R-1))
                if r > R:
                    shark[i][3] = 1
                    r = 2*R - r
                    if r < 1:
                        shark[i][3] = 2
                        r = 2 - r
            elif shark[i][3] == 3:
                c -= shark[i][2] % (2*(C-1))
                if c < 1:
                    shark[i][3] = 4
                    c = 2 - c
                    if c > C:
                        shark[i][3] = 3
                        c = 2*C - c
            elif shark[i][3] == 4:
                c += shark[i][2] % (2*(C-1))
                if c > C:
                    shark[i][3] = 3
                    c = 2*C - c
                    if c < 1:
                        shark[i][3] = 4
                        c = 2 - c
            shark[i][0] = r
            shark[i][1] = c
            if graph[r][c] == -1:
                graph[r][c] = i
            else: #같은 칸에 상어가 있으면 큰 놈이 살아남음
                j = graph[r][c]
                if shark[i][4] > shark[j][4]:
                    shark[j][5] = False
                    graph[r][c] = i
                else:
                    shark[i][5] = False

ans = 0
for i in range(1, C+1):
    for j in range(1, R+1):
        if graph[j][i] != -1:
            k = graph[j][i]
            ans += shark[k][4]
            shark[k][5] = False
            graph[j][i] = -1
            break
    move()

print(ans)