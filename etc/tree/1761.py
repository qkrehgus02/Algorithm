#쿼리가 10,000개까지 있으므로 O(N) 방식으로 LCS를 구하면 안됨
#root는 임의로 잡고 dfs를 돌리면 트리 형태로 재구성 가능
import sys 

sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n+1)]
parent = [[0 for _ in range(16)] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
dist = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b, weight = map(int, input().split())
    graph[a].append([b, weight])
    graph[b].append([a, weight])
    
def dfs(node, par, d, dist_val):
    depth[node] = d
    dist[node] = dist_val
    parent[node][0] = par 
    
    for next_node, weight in graph[node]:
        if next_node != par:
            dfs(next_node, node, d + 1, dist_val + weight)

dfs(1, 0, 0, 0)

for k in range(1, 16):
    for node in range(1, n+1):
        parent[node][k] = parent[parent[node][k-1]][k-1]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    
    diff = depth[u] - depth[v]
    for k in range(16):
        if diff & (1 << k):
            u = parent[u][k]
    
    if u == v:
        return u 
    
    for k in range(15, -1, -1):
        if parent[u][k] != parent[v][k]:
            u = parent[u][k]
            v = parent[v][k]
    
    return parent[u][0]

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    l = lca(u, v)
    print(dist[u] + dist[v] - 2 * dist[l])