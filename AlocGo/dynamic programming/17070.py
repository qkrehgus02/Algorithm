#화살표에 따라 가능한 경우 
# 1) 오른쪽 화살표 : 아래로는 갈 수 없음 (오른쪽, 대각선만 가능)
# 2) 아래 화살표 : 오른쪽으로는 갈 수 없음 (아래, 대각선만 가능)
# 3) 대각선 : 어디든 갈 수 있음 !

n= int(input())

graph = []

dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
# 3차원 배열 - n*n 크기의 그래프 상태를 나타내면서 각 위치에서의 화살표 방향도 저장
# 0 - 오른쪽 화살표로 도착 , 1 - 아래쪽 화살표로 도착 , 2 - 대각선 화살표로 도착

for _ in range(n):
    graph.append(list(map(int, input().split())))

dp[0][1][0] = 1
    
for i in range(n):
    for j in range(n):
        # 현재 위치가 벽이면 아무 전이도 하지 않음
        if graph[i][j] == 1:
            continue

        for k in range(3):
            # 0: 오른쪽, 1: 아래, 2: 대각선
            if k == 0:  # 오른쪽일 경우
                # 오른쪽 전이: 다음 칸이 벽이 아니어야 함
                if j + 1 < n and graph[i][j + 1] == 0:
                    dp[i][j + 1][0] += dp[i][j][0]
                # 대각선 전이: 세 칸 모두 벽이 아니어야 함
                if i + 1 < n and j + 1 < n and graph[i][j + 1] == 0 and graph[i + 1][j] == 0 and graph[i + 1][j + 1] == 0:
                    dp[i + 1][j + 1][2] += dp[i][j][0]

            elif k == 1:  # 아래쪽일 경우
                if i + 1 < n and graph[i + 1][j] == 0:
                    dp[i + 1][j][1] += dp[i][j][1]
                if i + 1 < n and j + 1 < n and graph[i][j + 1] == 0 and graph[i + 1][j] == 0 and graph[i + 1][j + 1] == 0:
                    dp[i + 1][j + 1][2] += dp[i][j][1]

            else:  # k == 2, 대각선일 경우
                if j + 1 < n and graph[i][j + 1] == 0:
                    dp[i][j + 1][0] += dp[i][j][2]
                if i + 1 < n and graph[i + 1][j] == 0:
                    dp[i + 1][j][1] += dp[i][j][2]
                if i + 1 < n and j + 1 < n and graph[i][j + 1] == 0 and graph[i + 1][j] == 0 and graph[i + 1][j + 1] == 0:
                    dp[i + 1][j + 1][2] += dp[i][j][2]


print(dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2])