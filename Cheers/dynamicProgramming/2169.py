n, m = map(int, input().split())

graph = []
temp = [0 for _ in range(m)]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    if(i == 0): #첫줄에는 무조건 한개의 경로
        for j in range(m):
            if j == 0:
                dp[i][j] = graph[i][j]
            else:
                dp[i][j] = dp[i][j-1] + graph[i][j]
    elif(i == n-1): #마지막 줄에는 2개의 경로
        for j in range(m):
            if j == 0:
                dp[i][j] = dp[i-1][j] + graph[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + graph[i][j]
    else: 
        for j in range(m): #왼쪽에서 오른쪽으로 탐색
            if j == 0 :
                temp[j] = dp[i-1][j] + graph[i][j]
            else:
                temp[j] = max(dp[i-1][j] , temp[j-1]) + graph[i][j]
        for k in range(m-1, -1, -1): #오른쪽에서 왼쪽으로 탐색
            if k == m-1:
                dp[i][k] = dp[i-1][k] + graph[i][k]
            else: #두 경우를 합침
                dp[i][k] = max(dp[i-1][k], dp[i][k+1]) + graph[i][k]
        for j in range(m):
            dp[i][j] = max(dp[i][j], temp[j])
        
print(dp[n-1][m-1])