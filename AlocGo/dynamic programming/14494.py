k = 1000000007

n, m = map(int, input().split())

dp = [[1 for _ in range(n+1)] for _ in range(m+1)]

for i in range(2, m+1):
    for j in range(2, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]

print(dp[m][n]%k)