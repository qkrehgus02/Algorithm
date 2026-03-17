n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))

parent = [i for i in range(n * m)]

def idx(i, j):
    return i * m + j

def find(k):
    if parent[k] == k:
        return k 
    return find(parent[k])

def union(a, b):
    parent[find(a)] = find(b)
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'U':
            if 0 <= i - 1 < n:
                union(idx(i, j), idx(i-1, j))
        elif graph[i][j] == 'D':
            if 0 <= i + 1 < n:
                union(idx(i, j), idx(i+1, j))
        elif graph[i][j] == 'L':
            if 0 <= j - 1 < m:
                union(idx(i, j), idx(i, j-1))
        elif graph[i][j] == 'R':
            if 0 <= j + 1 < m:
                union(idx(i, j), idx(i, j+1))

count = 0
for i in range(n * m):
    if find(i) == i:
        count += 1
print(count)
