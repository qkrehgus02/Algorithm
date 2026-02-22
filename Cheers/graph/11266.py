import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)] 
visited = [False for _ in range(v+1)] 
disc = [0 for _ in range(v+1)] 
low = [0 for _ in range(v+1)] 

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = 0

is_cut = [False] * (v+1)

def dfs(node, parent):
    global order
    order += 1
    disc[node] = low[node] = order
    child_count = 0

    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            child_count += 1
            dfs(child, node)
            low[node] = min(low[node], low[child])

            if parent != 0 and low[child] >= disc[node]:
                is_cut[node] = True
        elif child != parent:
            low[node] = min(low[node], disc[child])

    if parent == 0 and child_count >= 2:
        is_cut[node] = True

for i in range(1, v+1):
    if not visited[i]:
        visited[i] = True
        dfs(i, 0)

anslist = [i for i in range(1, v+1) if is_cut[i]]
anslist.sort()
print(len(anslist))
print(*anslist)

