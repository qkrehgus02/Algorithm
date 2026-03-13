import heapq

INF = 10**6
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 1

while True:
    n = int(input())

    if n == 0:
        break
    else:
        
        graph = []

        for _ in range(n):
            graph.append(list(map(int, input().split())))

        def dijkstra(graph, n):
            dist = [[INF for _ in range(n)] for _ in range(n)]
            dist[0][0] = graph[0][0]
            heap = []
            heapq.heappush(heap, (graph[0][0], 0, 0))

            while heap:
                cost, x, y = heapq.heappop(heap)

                if cost > dist[x][y]:
                    continue
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < n:
                        new_cost = cost + graph[nx][ny]
                        if new_cost < dist[nx][ny]:
                            dist[nx][ny] = new_cost
                            heapq.heappush(heap, (new_cost, nx, ny))
            return dist[n-1][n-1]

        print(f"Problem {count}: {dijkstra(graph, n)}")
    count += 1
