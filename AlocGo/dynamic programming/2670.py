n = int(input())

prime = []
dp = [0 for _ in range(n)]

for _ in range(n):
    prime.append(float(input()))

for i in range(n):
    dp[i] = max(prime[i]*dp[i-1], prime[i])

        
        
# 최대값 계산
result = max(dp)

# 소수점 넷째 자리에서 반올림 → 셋째 자리까지 출력
print(f"{result:.3f}")