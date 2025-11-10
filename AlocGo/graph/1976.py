n = int(input()) # 도시의 수
m = int(input()) # 여행 계획 도시의 수

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i, j)

possible = True

root = find(plan[0] - 1) # 첫번째 도시의 부모를 찾아서 루트로 활용

for i in range(1, m):
    if find(plan[i] - 1) != root:
        possible = False
        break

if possible:
    print("YES")   
else:
    print("NO")