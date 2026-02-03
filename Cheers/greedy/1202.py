n, k = map(int, input().split())

diamond = []
c_list = []

for _ in range(n):
    m, v = map(int, input().split())
    diamond.append([m, v, False])

for _ in range(k):
    c_list.append(int(input()))
    
c_list.sort()
diamond.sort(key=lambda x: (x[0], x[1]), reverse=True)

ans = 0

for c in c_list:
    for d in range(len(diamond)):
        if diamond[d][2] == False: #담지 않은 보석에 대해서만 탐색
            if diamond[d][0] <= c: #담을 수 있는 보석이라면
                diamond[d][2] = True #가방에 담고
                ans += diamond[d][1]
                break #반복문 종료
                #정렬이 되어 있기 때문에 제일 먼저 조건에 맞는 보석이 결국 우리가 찾는 보석임. 

print(ans)