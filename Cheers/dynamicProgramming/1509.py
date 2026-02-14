base = list(input())

n = len(base)

# 1) i->j가 팰린드롬인가?
palindrome = [[False for _ in range(n)] for _ in range(n)]

for gap in range(n):
    for i in range(n-gap):
        j = i + gap 
        if base[i] == base[j]:
            if gap <= 1:
                palindrome[i][j] = True
            elif palindrome[i+1][j-1]:
                palindrome[i][j] = True
                
dp = [0 for _ in range(n)]

for i in range(n):
    if i > 0 :
        dp[i] = dp[i-1] + 1 
    else :
        dp[i] = 1
    for j in range(i+1):
        if palindrome[j][i] == True:
            if j == 0:
                dp[i] = 1
            elif dp[i] > dp[j-1] + 1:
                dp[i] = dp[j-1] + 1

print(dp[n-1])