N = int(input())

INF = 100000
dpr = [[INF for _ in range(3)] for _ in range(N)]
dpg = [[INF for _ in range(3)] for _ in range(N)]
dpb = [[INF for _ in range(3)] for _ in range(N)]

for i in range(N):
    r, g, b = map(int, input().split())
    
    if i == 0:
        dpr[0][0] = r
        dpg[0][1] = g
        dpb[0][2] = b
    else:
        dpr[i][0] = min(dpr[i-1][1], dpr[i-1][2]) + r #빨간색을 고른다면 이전 색은 초록 or 파랑
        dpr[i][1] = min(dpr[i-1][0], dpr[i-1][2]) + g
        dpr[i][2] = min(dpr[i-1][0], dpr[i-1][1]) + b 
        
        dpg[i][0] = min(dpg[i-1][1], dpg[i-1][2]) + r #빨간색을 고른다면 이전 색은 초록 or 파랑
        dpg[i][1] = min(dpg[i-1][0], dpg[i-1][2]) + g
        dpg[i][2] = min(dpg[i-1][0], dpg[i-1][1]) + b 
        
        dpb[i][0] = min(dpb[i-1][1], dpb[i-1][2]) + r #빨간색을 고른다면 이전 색은 초록 or 파랑
        dpb[i][1] = min(dpb[i-1][0], dpb[i-1][2]) + g
        dpb[i][2] = min(dpb[i-1][0], dpb[i-1][1]) + b 
    
maxr = min(dpr[N-1][1], dpr[N-1][2])
maxg = min(dpg[N-1][0], dpg[N-1][2])
maxb = min(dpb[N-1][0], dpb[N-1][1])

print(min(maxr, maxg, maxb))