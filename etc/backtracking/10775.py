import sys
sys.setrecursionlimit(100000)

G = int(input())
P = int(input())

plane_list = []
parent = [i for i in range(G+1)]

count = 0

for _ in range(P):
    plane_list.append(int(input()))

def find(n):
    if n == parent[n]:
        return n
    parent[n] = find(parent[n])
    return parent[n]

for plane in plane_list:
    if find(plane) == 0:
        break
    else:
        count += 1
        gate = find(plane)
        parent[gate] = gate - 1

print(count)