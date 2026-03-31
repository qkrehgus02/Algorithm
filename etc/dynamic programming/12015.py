n = int(input())
a = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(i-1, -1, -1):
        if a[i] > a[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(dp[0])