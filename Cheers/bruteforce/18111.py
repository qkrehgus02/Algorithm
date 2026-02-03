N, M, B = map(int, input().split())
min = 10000000000
max = 0
ground = []
time = 0
min_time = 100000000
height = 0

for _ in range(N):
    row = list(map(int, input().split()))
    ground.append(row)

for i in range(N):
    for j in range(M):
        if max < ground[i][j]:
            max = ground[i][j]
        if min > ground[i][j]:
            min = ground[i][j]

for i in range(min, max + 1):
    inv = B
    time = 0

    for j in range(N):
        for k in range(M):
            diff = ground[j][k] - i
            inv += diff

            if diff > 0:
                time += diff * 2  
            else:
                time -= diff

    if inv >= 0:
        if min_time >= time:
            min_time = time
            height = i

print(min_time, height)