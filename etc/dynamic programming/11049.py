n = int(input())
INF = 10**32

procession = []
dp = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    r, c = map(int, input().split())
    procession.append([r, c])
    
for gap in range(1, n):
    for a in range(0, n - gap):
        b = a + gap
        min = INF
        for k in range(a, b):
            now = dp[a][k] + dp[k+1][b] + procession[a][0] * procession[k][1] * procession[b][1]
            if now < min:
                min = now
        dp[a][b] = min

print(dp[0][n-1])