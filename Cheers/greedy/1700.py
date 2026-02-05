#OPT 알고리즘 
#가장 나중에 쓰일 것을 제거

INF = 10000000000

n, k = map(int, input().split())
elec = list(map(int, input().split()))

multitab = []
size = 0
ans = 0

nextuse = [INF for _ in range(k+1)]

for e in range(len(elec)):
    if nextuse[elec[e]] == INF:
        nextuse[elec[e]] = e

def update(num):
    for i in range(num+1, len(elec)):
        if elec[i] == elec[num]:
            return i
    return INF
    
for e in range(len(elec)):
    if size < n: #멀티탭에 자리가 있으면 꼽고. 
        if elec[e] not in multitab:
            multitab.append(elec[e])
            size += 1
    else: #멀티탭에 자리가 없고
        if elec[e] not in multitab: #교체가 필요하면
            victim = multitab[0]
            max_val = nextuse[multitab[0]]
            for m in multitab:
                if nextuse[m] > max_val:
                    max_val = nextuse[m]
                    victim = m
            multitab.remove(victim)
            multitab.append(elec[e])
            ans += 1
    nextuse[elec[e]] = update(e)
    
print(ans)