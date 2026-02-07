from collections import deque

t = int(input())
ans = []

for _ in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)] #noncycle, directed
    indegree = [0 for _ in range(n+1)] #진입차수 체크 -> 진입차수가 낮은 애들부터 체크(위상정렬)
    dp = [0 for _ in range(n+1)] #dp를 통해 특정 노드까지의 걸리는 최솟값 저장
    queue = deque() #위상정렬을 위한 queue

    for _ in range(k): 
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(input())

    for i in range(1, n+1): #initialize
        if indegree[i] == 0: #진입차수가 0이면
            queue.append(i) #Queue에 넣음
            dp[i] = time[i-1] #dp값도 미리 설정

    while queue:
        now = queue.popleft() #queue에서 값을 하나 꺼내서

        for i in graph[now]: #그래프를 돌며
            indegree[i] -= 1
            dp[i] = max(dp[i] , dp[now] + time[i-1]) #dp 배열 갱신
            if indegree[i] == 0: #진입차수가 0일때만 그래프에 !!!
                queue.append(i) #그래프에 넣고
            

    ans.append(dp[w])

for i in ans:
    print(i)