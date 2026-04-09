from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 1] for _ in range(n+1)]
parent = [0] * (n+1)
visited = [False] * (n+1)
order = []

queue = deque([1])
visited[1] = True

while queue:
    node = queue.popleft()
    order.append(node)
    for next in tree[node]:
        if not visited[next]:
            visited[next] = True
            parent[next] = node
            queue.append(next)

for node in reversed(order):
    for next in tree[node]:
        if next == parent[node]:
            continue
        dp[node][1] += min(dp[next][0], dp[next][1])
        dp[node][0] += dp[next][1]

print(min(dp[1][0], dp[1][1]))
