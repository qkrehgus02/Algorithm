n = int(input())
w_list = list(map(int, input().split()))

w_list.sort()

ans = 1

for w in w_list:
    if ans < w: #연속된 수를 못 만들면
        break
    else: #만들 수 있음
        ans += w

print(ans)