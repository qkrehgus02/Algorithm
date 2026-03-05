TC = int(input())

INF = int(1e9)

result = []

for _ in range(TC):
    N, M, W = map(int, input().split())
    
    edges = []
    
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
        
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))
    
    def bellman_ford():
        distance = [0] * (N + 1)
        
        for i in range(1, N+1):
            for j in range(2 * M + W):
                cur_node = edges[j][0]
                next_node = edges[j][1]
                edge_cost = edges[j][2]
                
                if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                    distance[next_node] = distance[cur_node] + edge_cost
                    if i == N :
                        return True
        return False
    
    ans = "NO"
    

    if bellman_ford() == True:
        ans = "YES"
    
    result.append(ans)

for r in result:
    print(r)