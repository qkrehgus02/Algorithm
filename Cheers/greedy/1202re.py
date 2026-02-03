import heapq

n, k = map(int, input().split())

diamond = []
c_list = []

for _ in range(n):
    m, v = map(int, input().split())
    diamond.append([m, v])

for _ in range(k):
    c_list.append(int(input()))
    
c_list.sort()
diamond.sort(key=lambda x: x[0])

heap = []

idx = 0
ans = 0

for c in c_list:
    while idx < n and diamond[idx][0] <= c:
        heapq.heappush(heap, -diamond[idx][1])
        idx += 1
    if heap:
        ans -= heapq.heappop(heap)

print(ans)