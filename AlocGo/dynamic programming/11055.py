n = int(input())
A = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = A[0]

for i in range(1, n):
    dp[i] = A[i]
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])    

print(max(dp))