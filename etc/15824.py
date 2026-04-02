# sc[k] * (2^k - 1) - sc[k] * (2^(n-1-k) - 1) 

n = int(input())
sc = list(map(int, input().split()))

sc.sort()

MOD = 1000000007
ans = 0

pow2 = [1] * n
for i in range(1, n):
    pow2[i] = pow2[i-1] * 2 % MOD

for k in range(n):
    ans += sc[k] * (pow2[k] - 1) - sc[k] * (pow2[n-1-k] - 1)
    ans = (ans % MOD + MOD) % MOD

print(ans)